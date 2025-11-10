import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar
)
from PySide6.QtCore import QTimer, Qt
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 200)
    else:
        print("\a")

class PomodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodo - Work")
        self.setFixedSize(300, 200)
        self.init_ui()
        self.init_state()

    def init_ui(self):
        layout = QVBoxLayout()

        self.timer_label = QLabel("25:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 36px;")
        layout.addWidget(self.timer_label)

        self.progress = QProgressBar()
        self.progress.setMaximum(100)  # percentage of current session
        self.progress.setValue(0)
        self.progress.setTextVisible(True)
        layout.addWidget(self.progress)

        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.toggle_timer)
        layout.addWidget(self.start_btn)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)

    def init_state(self):
        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.current_time = self.work_time
        self.total_time = self.work_time  # used for progress percentage
        self.in_break = False
        self.is_running = False

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

    def toggle_timer(self):
        if self.is_running:
            self.timer.stop()
            self.start_btn.setText("Start")
        else:
            self.timer.start()
            self.start_btn.setText("Pause")
        self.is_running = not self.is_running

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.start_btn.setText("Start")
        self.current_time = self.total_time
        self.update_timer_label()
        self.update_progress()

    def update_timer(self):
        if self.current_time > 0:
            self.current_time -= 1
            self.update_timer_label()
            self.update_progress()
        else:
            self.timer.stop()
            self.is_running = False
            self.start_btn.setText("Start")
            self.handle_session_end()

    def update_timer_label(self):
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def update_progress(self):
        percent = int((self.total_time - self.current_time) / self.total_time * 100)
        self.progress.setValue(percent)

    def handle_session_end(self):
        beep()

        if self.in_break:
            # Break ended → start work
            self.in_break = False
            self.current_time = self.work_time
            self.total_time = self.work_time
            self.setWindowTitle("Pomodo - Work")
        else:
            # Work ended → start break
            self.in_break = True
            self.current_time = self.short_break
            self.total_time = self.short_break
            self.setWindowTitle("Pomodo - Short Break")

        self.update_timer_label()
        self.update_progress()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoApp()
    window.show()
    sys.exit(app.exec())
