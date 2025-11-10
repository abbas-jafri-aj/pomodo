import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QCheckBox
from PySide6.QtCore import QTimer, Qt
from playsound3 import playsound


class PomodoroApp(QWidget):
    def __init__(self, work_minutes=25, short_break_minutes=5, long_break_minutes=15, sessions_before_long_break=4):
        super().__init__()

        # Timer durations in seconds (allow fractional minutes)
        self.work_time = round(work_minutes * 60)
        self.short_break = round(short_break_minutes * 60)
        self.long_break = round(long_break_minutes * 60)
        self.sessions_before_long_break = sessions_before_long_break

        # State
        self.time_left = self.work_time
        self.is_running = False
        self.current_session = 'work'
        self.completed_work_sessions = 0

        # GUI Setup
        self.setFixedSize(320, 200)  # window width
        layout = QVBoxLayout()

        # Timer label
        self.timer_label = QLabel(self.format_time(self.time_left))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 36px;")
        layout.addWidget(self.timer_label)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, self.work_time)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Start/Pause button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggle_timer)
        layout.addWidget(self.start_button)

        # Reset button
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_button)

        # Play Sound checkbox
        self.sound_checkbox = QCheckBox("Play Sound")
        self.sound_checkbox.setChecked(True)
        layout.addWidget(self.sound_checkbox)

        self.setLayout(layout)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Initialize window title
        self.update_window_title()

    def format_time(self, seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    def toggle_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_button.setText("Start")
        else:
            self.timer.start(1000)
            self.is_running = True
            self.start_button.setText("Pause")

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.current_session = 'work'
        self.completed_work_sessions = 0
        self.time_left = self.work_time
        self.progress_bar.setRange(0, self.work_time)
        self.progress_bar.setValue(0)
        self.timer_label.setText(self.format_time(self.time_left))
        self.start_button.setText("Start")
        self.update_window_title()

    def update_window_title(self):
        if self.current_session == 'work':
            session_number = self.completed_work_sessions + 1
            title = f"Pomodo - Work Session {session_number}"
        elif self.current_session == 'short_break':
            session_number = self.completed_work_sessions
            title = f"Pomodo - Short Break {session_number}"
        else:  # long_break
            title = "Pomodo - Long Break"
        self.setWindowTitle(title)

    def get_current_session_total(self):
        if self.current_session == 'work':
            return self.work_time
        elif self.current_session == 'short_break':
            return self.short_break
        else:
            return self.long_break

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(self.format_time(self.time_left))
            self.progress_bar.setValue(self.get_current_session_total() - self.time_left)
        else:
            # Play beep if checkbox is checked
            if self.sound_checkbox.isChecked():
                playsound("beep.wav")

            # Move to next session
            if self.current_session == 'work':
                self.completed_work_sessions += 1
                if self.completed_work_sessions == self.sessions_before_long_break:
                    self.current_session = 'long_break'
                    self.time_left = self.long_break
                else:
                    self.current_session = 'short_break'
                    self.time_left = self.short_break

            elif self.current_session == 'short_break':
                self.current_session = 'work'
                self.time_left = self.work_time

            else:  # long_break
                # Auto-reset after long break
                self.reset_timer()
                return  # exit early

            # Update GUI for next session
            self.progress_bar.setRange(0, self.get_current_session_total())
            self.progress_bar.setValue(0)
            self.timer_label.setText(self.format_time(self.time_left))
            self.update_window_title()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Example: fast cycle for testing (fractional minutes)
    window = PomodoroApp(work_minutes=0.1, short_break_minutes=0.05, long_break_minutes=0.1)
    window.show()

    sys.exit(app.exec())
