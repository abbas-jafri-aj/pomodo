# Pomodo Timer

A simple and functional Pomodoro Timer built with Python and PyQt6.

---

## Features
- Work sessions and breaks (short and long)
- Auto-cycles through work and break sessions
- Resets automatically after completing all sessions
- "Start" button toggles to "Pause" while running
- Optional sound alert (configurable with a checkbox)
- Clean, compact 320px-wide interface

---

## Installation and Running Instructions

### Step 1: (Optional) Install and Pin Python 3.11 using `uv`

If you don’t have Python 3.11 installed or want to ensure the correct version:

```
uv python install 3.11
uv python pin 3.11
```

---

### Step 2: Create Virtual Environment

You can create the virtual environment using either **uv** or Python’s built-in **venv** module.

**Option 1: Using uv**
```
uv venv .venv
```

**Option 2: Using Python**
```
python -m venv .venv
```

---

### Step 3: Activate the Virtual Environment

**On Windows (PowerShell):**
```
.\.venv\Scripts\activate
```

**On Linux or macOS:**
```
source .venv/bin/activate
```

---

### Step 4: Ensure pip is installed and upgraded
```
python -m ensurepip
python -m pip install --upgrade pip
```

---

### Step 5: Install Required Packages
```
python -m pip install -r requirements.txt
```

---

### Step 6: Run the Pomodoro Timer
```
python .\pomodo.py
```

---

### Step 7: Deactivate the Virtual Environment
```
deactivate
```

---

### Step 8: (Optional) Uninstall Python 3.11 if Installed via uv
```
uv python uninstall 3.11
```

---

## Notes
- The app automatically resets after completing all sessions.
- Use the “Play Sound” checkbox to toggle the completion alert.
- The long break has no session suffix in the title.

---

## Requirements
- Python 3.11+
- PyQt6
