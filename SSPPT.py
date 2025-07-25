import tkinter as tk
from tkinter import messagebox
import json
import os
import re

DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                return []
            return tasks
    except Exception:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def validate_time_format(timestr):
    # Validate HH:MM:SS format and that HH,MM,SS are within proper ranges
    pattern = r'^(\d{1,2}):([0-5]\d):([0-5]\d)$'
    match = re.match(pattern, timestr)
    if not match:
        return False
    h, m, s = map(int, match.groups())
    if h < 0 or m < 0 or m > 59 or s < 0 or s > 59:
        return False
    return True

def time_str_to_seconds(timestr):
    h, m, s = map(int, timestr.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time_str(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


class TimerWindow:
    def __init__(self, master, title, total_seconds):
        self.master = tk.Toplevel(master)
        self.master.title(title)
        self.master.geometry("300x180")
        self.master.resizable(False, False)

        self.total_seconds = total_seconds
        self.remaining_seconds = total_seconds
        self.is_running = False
        self._timer_id = None

        # Timer label HH:MM:SS
        self.label_timer = tk.Label(self.master, text=seconds_to_time_str(self.remaining_seconds),
                                    font=("Arial", 36), fg="darkblue")
        self.label_timer.pack(pady=15)

        # Buttons
        btn_frame = tk.Frame(self.master)
        btn_frame.pack(pady=10)

        self.btn_start = tk.Button(btn_frame, text="START", width=8, command=self.start_timer)
        self.btn_start.pack(side=tk.LEFT, padx=5)

        self.btn_stop = tk.Button(btn_frame, text="STOP", width=8, command=self.stop_timer)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        self.btn_reset = tk.Button(btn_frame, text="RESET", width=8, command=self.reset_timer)
        self.btn_reset.pack(side=tk.LEFT, padx=5)

        # Made by label bottom left
        self.label_credit = tk.Label(self.master, text="Made by SSPPT", font=("Arial", 9, "italic"))
        self.label_credit.pack(side=tk.BOTTOM, anchor='w', padx=5, pady=5)

        # When closing timer window, stop timer loop
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_timer_label(self):
        self.label_timer.config(text=seconds_to_time_str(self.remaining_seconds))

    def countdown(self):
        if self.is_running and self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.update_timer_label()
            self._timer_id = self.master.after(1000, self.countdown)
        elif self.remaining_seconds == 0:
            self.is_running = False
            self.update_timer_label()
            messagebox.showinfo("Timer Finished", "Time is up!")

    def start_timer(self):
        if not self.is_running and self.remaining_seconds > 0:
            self.is_running = True
            self.countdown()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            if self._timer_id is not None:
                self.master.after_cancel(self._timer_id)
                self._timer_id = None

    def reset_timer(self):
        self.stop_timer()
        self.remaining_seconds = self.total_seconds
        self.update_timer_label()

    def on_close(self):
        self.stop_timer()
        self.master.destroy()

# This is the main window where users can input task details
class TaskInputWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Task")
        self.master.geometry("350x180")
        self.master.resizable(False, False)

        # Task Title Label + Entry
        tk.Label(master, text="Task Title:", font=("Arial", 12)).place(x=15, y=15)
        self.entry_title = tk.Entry(master, font=("Arial", 12))
        self.entry_title.place(x=110, y=15, width=210)

        # Task Time Label + Entry (HH:MM:SS)
        tk.Label(master, text="Task Time (HH:MM:SS):", font=("Arial", 12)).place(x=15, y=60)
        self.entry_time = tk.Entry(master, font=("Arial", 12))
        self.entry_time.place(x=190, y=60, width=130)
        self.entry_time.insert(0, "00:25:00")  # default 25 min

        # Add Task Button
        self.btn_add = tk.Button(master, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.btn_add.place(x=20, y=110, width=100, height=30)
        
        # Show All Task Button
        self.btn_show = tk.Button(master, text="Show All Task", font=("Arial", 12), command=self.show_all_tasks)
        self.btn_show.place(x=180, y=110, width=140, height=30)

        # Made by label bottom left
        tk.Label(master, text="Made by SSPPT", font=("Arial", 9, "italic")).place(x=10, y=150)

    def add_task(self):
        title = self.entry_title.get().strip()
        time_str = self.entry_time.get().strip()

        if not title:
            messagebox.showwarning("Input Error", "Please enter a Task Title.")
            return

        if not validate_time_format(time_str):
            messagebox.showwarning("Input Error", "Please enter time in valid HH:MM:SS format.")
            return

        total_seconds = time_str_to_seconds(time_str)
        if total_seconds == 0:
            messagebox.showwarning("Input Error", "Task time must be greater than 00:00:00.")
            return

        # Load existing tasks
        tasks = load_tasks()

        # Save new task to list
        tasks.append({"title": title, "time_seconds": total_seconds})

        save_tasks(tasks)

        # Close this window and open timer window
        self.master.withdraw()  # Hide first window
        TimerWindow(self.master, title, total_seconds)

    def show_all_tasks(self):
        tasks = load_tasks()

        if not tasks:
            messagebox.showinfo("All Tasks", "No tasks saved yet.")
            return

        popup = tk.Toplevel(self.master)
        popup.title("All Saved Tasks")
        popup.geometry("300x300")
        popup.resizable(False, False)

        # Listbox to show tasks
        listbox = tk.Listbox(popup, font=("Arial", 12))
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for i, t in enumerate(tasks, start=1):
            time_fmt = seconds_to_time_str(t.get("time_seconds", 0))
            listbox.insert(tk.END, f"{i}. {t['title']}  -  {time_fmt}")

        # Made by Label
        tk.Label(popup, text="Made by SSPPT", font=("Arial", 9, "italic")).pack(side=tk.BOTTOM, anchor='w', padx=5, pady=5)

        # Focus on popup so user can close before main window
        popup.transient(self.master)
        popup.grab_set()
        self.master.wait_window(popup)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskInputWindow(root)
    root.mainloop()

