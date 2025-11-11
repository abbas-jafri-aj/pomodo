import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from playsound3 import playsound

class Pomodo:
    def __init__(self, work_time=25, short_break=5, long_break=15):
        # Configurable times in minutes
        self.work_time = work_time
        self.short_break = short_break
        self.long_break = long_break

        self.sessions_completed = 0
        self.current_session = 'work'
        self.remaining = int(self.work_time * 60)
        self.is_running = False

        # Main window
        self.root = ttk.Window(title=self.get_title(), themename="litera", size=(400, 400))
        
        # Timer label
        self.timer_label = ttk.Label(self.root, text=self.format_time(self.remaining), font=("Arial", 24))
        self.timer_label.pack(pady=10)

        # Meter (replaces Progressbar)
        self.meter = ttk.Meter(
            self.root,
            metersize=180,
            amountused=0,
            amounttotal=int(self.work_time * 60),
            stripethickness=10,
            # subtext="Progress",
            textright="s",
            bootstyle="primary",
            subtextstyle="info",
        )
        self.meter.pack(pady=5)

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        self.start_btn = ttk.Button(btn_frame, text="Start", width=10, command=self.toggle)
        self.start_btn.pack(side=LEFT, padx=5)
        self.reset_btn = ttk.Button(btn_frame, text="Reset", width=10, command=self.reset)
        self.reset_btn.pack(side=LEFT, padx=5)

        # Play sound checkbox
        self.play_sound_var = ttk.BooleanVar(value=True)
        self.sound_cb = ttk.Checkbutton(self.root, text="Play Sound", variable=self.play_sound_var)
        self.sound_cb.pack(pady=5)

        # Timer tick
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
                total = int(self.get_current_session_time() * 60)
                used = total - self.remaining
                self.meter.configure(amountused=used, amounttotal=total)
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

        # Reset after long break
        if self.current_session == 'work' and self.sessions_completed >= 4:
            self.reset()
        else:
            self.meter.configure(amountused=0, amounttotal=int(self.get_current_session_time() * 60))
            self.timer_label.config(text=self.format_time(self.remaining))

    def reset(self):
        self.is_running = False
        self.start_btn.config(text="Start")
        self.sessions_completed = 0
        self.current_session = 'work'
        self.remaining = int(self.work_time * 60)
        self.timer_label.config(text=self.format_time(self.remaining))
        self.meter.configure(amountused=0, amounttotal=int(self.work_time * 60))
        self.root.title(self.get_title())

if __name__ == "__main__":
    # For testing fast cycles
    # Pomodo(work_time=0.1, short_break=0.05, long_break=0.08)
    Pomodo()
