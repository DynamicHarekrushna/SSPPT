import tkinter as tk
from tkinter import messagebox
import json
import os
import re

DATA_FILE = 'tasks.json'

class TaskInputWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Task")
        self.master.geometry("350x180")
        self.master.resizable(False, False)

        #Title
        tk.Label(master, text="Task Title:", font=("Arial", 12)).place(x=15, y=15)
        self.entry_title = tk.Entry(master, font=("Arial", 12))
        self.entry_title.place(x=110, y=15, width=210)

        # Time (HH:MM:SS)
        tk.Label(master, text="Task Time (HH:MM:SS):", font=("Arial", 12)).place(x=15, y=60)
        self.entry_time = tk.Entry(master, font=("Arial", 12))
        self.entry_time.place(x=190, y=60, width=130)
        self.entry_time.insert(0, "00:25:00")  # default 25 min

        # Add Button
        self.btn_add = tk.Button(master, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.btn_add.place(x=20, y=110, width=100, height=30)
        
        # Show All Button
        self.btn_show = tk.Button(master, text="Show All Task", font=("Arial", 12), command=self.show_all_tasks)
        self.btn_show.place(x=180, y=110, width=140, height=30)

        # Made by label bottom left
        tk.Label(master, text="Made by SSPPT", font=("Arial", 9, "italic")).place(x=10, y=150)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskInputWindow(root)
    root.mainloop()
