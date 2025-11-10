# Pomodo

A minimalist Pomodoro desktop timer built with **Python 3.11** and **PySide6**.
Simple interface. Does one job well. Helps you focus.

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/abbas-jafri-aj/pomodo.git
cd pomodo

# Create a virtual environment
python3.11 -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Run the app
python pomodo.py

To switch to another version later, just run:

uv python install 3.12
uv python pin 3.12
