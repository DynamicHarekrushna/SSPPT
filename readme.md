# Smart Study Planner with Pomodoro Timer

A minimalistic, cross-platform Python application for task-based study planning and focused time management using Pomodoro sessions. Built with Tkinter for the **GUI** and **JSON** for persistent local storage.

## 🚀 Features

- **Task Management:** Add multiple study tasks with custom Pomodoro durations.
- **Custom Pomodoro Timer:** Input any duration in `HH:MM:SS` (e.g., `00:25:00` for 25 minutes).
- **Persistent Data:** All tasks are saved in a local JSON file and persist between sessions.
- **Intuitive Dual-Window Interface:**
  - **Window 1:** Add new tasks, specify durations, and view all saved tasks.
  - **Window 2:** For each task, a dedicated timer window with Start, Stop, and Reset functions.
- **Input Validation:** Ensures time is always in proper `HH:MM:SS` format for reliability.
- **Clean UI:** Compact, distraction-free layout inspired by productivity minimalist principles.
- **Fully beginner-friendly:** Easy to understand, modify, and expand.

## 📂 File Structure
```
/project-root
│
├── SSPPT.py # Complete Smart Study Planner with Pomodoro Timer
├── tasks.json # Local storage for persistent user tasks (auto-created)
├── README.md
└── ...
```

_For simple projects, all classes can be in one file (e.g., `SSPPT.py`) as well._

## ⚡ Quick Start

1. **Clone this repository:**
    ```
    git clone https://github.com/your-username/smart-study-planner.git
    cd SSPPT
    ```

2. **Run the app:**
    ```
    python SSPPT.py
    ```

3. **Requirements:**
    - Python 3.x (3.6+ recommended)
    - No external dependencies—Tkinter and json are built-in

## 🛠️ Usage

1. **Add a Task**  
   Enter your task's title and desired time (`HH:MM:SS`) in the interface.  
   Click **"Add Task"** to save and launch a Pomodoro window.

2. **Manage Your Timer**  
   Use **START** to begin countdown, **STOP** to pause, and **RESET** to return to the original time.  
   Timer counts down in real time and informs you when time is up.

3. **View All Tasks**  
   Press **"Show All Task"** to see a popup of all stored tasks and their durations anytime.

## 💾 Data Persistence

- All tasks and timings are stored in a local file called `tasks.json`.
- Closing and reopening the program retains your entire task list for future use.

## 📚 Code Guide

- **TaskInputWindow:** Handles the first window, user input, validation, and creation of new TimerWindow instances.
- **TimerWindow:** Manages live countdown timer, and start/stop/reset buttons.
- **data_utils.py:** (optional for modular projects) Includes all JSON and time conversion logic.

Check commented sections in the code for further guidance on function and class roles.

## 👥 Collaboration

This project was collaboratively developed by HK & Payal.  

## 🤔 FAQ

**Q: Can I use this for things other than studying?**  
A: Yes! Add any task and set a timer—works for work sessions, exercise, breaks, and more.

**Q: Time input isn't working!**  
A: Ensure your input matches `HH:MM:SS` (`00:25:00` for 25 minutes, for example). Only values between `00:00:01` and `99:59:59` are valid.

**Q: Where is my data stored?**  
A: All your tasks are in `tasks.json` in the app directory.

## 🏷️ Keywords

python, tkinter, pomodoro, productivity, study-planner, json, gui, timer, task-management, minimalist, open-source

---

                                                Built with Python and discipline. 
                                                       Made by HK & Payal
