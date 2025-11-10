import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from playsound3 import playsound

class Pomodo:
    def __init__(self):
        # Configurable times in minutes
        self.work_time = 25
        self.short_break = 5
        self.long_break = 15

        # For testing fast cycles
        self.work_time = 0.1
        self.short_break = 0.05
        self.long_break = 0.08

        self.sessions_completed = 0
        self.current_session = 'work'
        self.remaining = int(self.work_time * 60)
        self.is_running = False

        # Create main window
        self.root = ttk.Window(title=self.get_title(), themename="litera", size=(400,200))
        
        # Timer label
        self.timer_label = ttk.Label(self.root, text=self.format_time(self.remaining), font=("Arial", 24))
        self.timer_label.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, length=280, mode='determinate')
        self.progress.pack(pady=5)

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        self.start_btn = ttk.Button(btn_frame, text="Start", width=10, command=self.toggle)
        self.start_btn.pack(side=LEFT, padx=5)
        self.reset_btn = ttk.Button(btn_frame, text="Reset", width=10, command=self.reset)
        self.reset_btn.pack(side=LEFT, padx=5)

        # Play Sound checkbox
        self.play_sound_var = ttk.BooleanVar(value=True)
        self.sound_cb = ttk.Checkbutton(self.root, text="Play Sound", variable=self.play_sound_var)
        self.sound_cb.pack(pady=5)

        self.root.after(1000, self.tick)
        self.root.mainloop()

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{int(m):02d}:{int(s):02d}"

    def get_current_session_time(self):
        if self.current_session == 'work':
            return self.work_time
        elif self.current_session == 'short_break':
            return self.short_break
        else:
            return self.long_break

    def get_title(self):
        if self.current_session == 'work':
            return f"Pomodo - Work Session {self.sessions_completed + 1}"
        elif self.current_session == 'short_break':
            return f"Pomodo - Short Break {self.sessions_completed}"
        else:
            return "Pomodo - Long Break"

    def toggle(self):
        if self.is_running:
            self.is_running = False
            self.start_btn.config(text="Start")
        else:
            self.is_running = True
            self.start_btn.config(text="Pause")

    def tick(self):
        if self.is_running:
            if self.remaining > 0:
                self.remaining -= 1
                self.timer_label.config(text=self.format_time(self.remaining))
                self.progress['maximum'] = int(self.get_current_session_time() * 60)
                self.progress['value'] = int(self.get_current_session_time() * 60 - self.remaining)
            else:
                self.end_session()
        self.root.after(1000, self.tick)

    def end_session(self):
        if self.play_sound_var.get():
            try:
                playsound("beep.wav")
            except Exception as e:
                print("Beep failed:", e)

        if self.current_session == 'work':
            self.sessions_completed += 1
            if self.sessions_completed % 4 == 0:
                self.current_session = 'long_break'
            else:
                self.current_session = 'short_break'
        else:
            self.current_session = 'work'

        if self.current_session == 'long_break':
            self.remaining = int(self.long_break * 60)
        elif self.current_session == 'short_break':
            self.remaining = int(self.short_break * 60)
        else:
            self.remaining = int(self.work_time * 60)

        self.root.title(self.get_title())

        # Auto-reset after long break
        if self.current_session == 'work' and self.sessions_completed >= 4:
            self.reset()

    def reset(self):
        self.is_running = False
        self.start_btn.config(text="Start")
        self.sessions_completed = 0
        self.current_session = 'work'
        self.remaining = int(self.work_time * 60)
        self.timer_label.config(text=self.format_time(self.remaining))
        self.progress['value'] = 0
        self.root.title(self.get_title())

if __name__ == "__main__":
    Pomodo()
