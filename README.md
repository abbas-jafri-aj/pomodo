# Pomodo – A Simple Pomodoro Timer

A lightweight, modern-themed Pomodoro Timer built with Python and ttkbootstrap.

---

## Step 1: (Optional) Install and Pin Python using `uv`

The app was tested on Python 3.14 and works fine.
This step is only needed if a user runs into Python version issues.

```
uv python install 3.11
uv python pin 3.11
```

---

## Step 2: Create and Activate a Virtual Environment

Create a virtual environment using either `uv` or Python’s built-in `venv`:

# Using uv
uv venv .venv

# OR using Python directly
python -m venv .venv

Activate the environment:

# Windows
.\.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

---

## Step 3: Install Dependencies

Upgrade pip and install required packages:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

---

## Step 4: Run the App

python pomodo.py

---

## Step 5: Deactivate the Virtual Environment

deactivate

---

## Notes

- The app automatically plays a beep sound at the end of each session.  
- You can reset the app using the Reset button.  
- The “Play Sound” checkbox allows you to toggle sound on or off.  
- All GUI elements are powered by `ttkbootstrap` for a modern, themed interface.  
- Optional Python version management is only needed if a user encounters version issues.
