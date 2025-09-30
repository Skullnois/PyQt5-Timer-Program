# 6/4/25: Can now start the timer and the timer stops when the clock hits zero.
# 6/5/25: Created a message box for when time runs out.
# 6/5/25: Created a reset button that resets the timer.
# 6/5/25: Created a pause and resume button.
# 6/5/25: New Mission: Sort out the code before trying to have you adjust the time on the GUI.
# 6/6/25: New Mission: Create the layout of the project.

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QMessageBox,
                             QGridLayout, QWidget, QLineEdit)
from PyQt5.QtCore import QTimer, Qt
from functionality import Timer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setStyleSheet("background-color:#684599;"
                           "color:white;")
        self.setWindowTitle("Timer App")
        self.title = QLabel("Timer", self)

        self.chosen_hours = 9
        self.chosen_minutes = 0
        self.chosen_seconds = 0

        # Sets up time and time label.
        self.time_left = 0
        self.time_label = QLabel(f"00:00:00", self)

        # Create the buttons
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        self.pause_resume_button = QPushButton("Pause", self)
        self.hour_plus = QPushButton("+", self)
        self.minute_plus = QPushButton("+", self)
        self.second_plus = QPushButton("+", self)
        self.hour_minus = QPushButton("-", self)
        self.minute_minus = QPushButton("-", self)
        self.second_minus = QPushButton("-", self)
        self.set_button = QPushButton("Set", self)
        self.timer_up_button = QPushButton("+30 sec", self)
        self.timer_down_button = QPushButton("-30 sec", self)

        # Numbers for settings
        self.hour_label = QLabel("Hours")
        self.minute_label = QLabel("Minutes")
        self.second_label = QLabel("Seconds")

        self.hour_label2 = QLineEdit("00", self)
        self.minute_label2 = QLineEdit("00", self)
        self.second_label2 = QLineEdit("00", self)

        self.my_format = ""

        self.format_labels()

        # instantiate Qtimer class and custom class Timer
        self.timer = Timer()
        self.qtime = QTimer()

        # Format and display the time left.
        self.set_up_timer()

        self.ui_design()
        self.ui()

    # Gives signals to the buttons.
    def ui(self):
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        self.pause_resume_button.clicked.connect(self.pause)

        self.hour_plus.clicked.connect(self.increase_hour_label)
        self.hour_minus.clicked.connect(self.decrease_hour_label)
        self.minute_plus.clicked.connect(self.increase_minute_label)
        self.minute_minus.clicked.connect(self.decrease_minute_label)
        self.second_plus.clicked.connect(self.increase_second_label)
        self.second_minus.clicked.connect(self.decrease_second_label)
        self.set_button.clicked.connect(self.change_timer)
        self.timer_up_button.clicked.connect(self.add_time)
        self.timer_down_button.clicked.connect(self.subtract_time)

        self.hour_label2.editingFinished.connect(self.change_hour_label)
        self.minute_label2.editingFinished.connect(self.change_minute_label)
        self.second_label2.editingFinished.connect(self.change_second_label)

    # Designs the GUI
    def ui_design(self):
        # Designs time label
        self.time_label.setStyleSheet("color:white;"
                                      "font-size:20px;")
        self.time_label.setGeometry((self.width() - self.time_label.width()) // 2,
                                    (self.height() - self.time_label.height()) // 2,
                                    self.time_label.width(),
                                    self.time_label.height())

        # Edit Title
        self.title.setStyleSheet("color:White;"
                                 "font-size:30px;")

        # Position buttons
        self.hour_label.setStyleSheet("color:white;"
                                      "font-size:15px;")

        self.minute_label.setStyleSheet("color:white;"
                                        "font-size:15px;")
        self.second_label.setStyleSheet("color:white;"
                                        "font-size:15px;")

        # Align the labels
        self.hour_label.setAlignment(Qt.AlignCenter)
        self.minute_label.setAlignment(Qt.AlignCenter)
        self.second_label.setAlignment(Qt.AlignCenter)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.hour_label2.setAlignment(Qt.AlignCenter)
        self.minute_label2.setAlignment(Qt.AlignCenter)
        self.second_label2.setAlignment(Qt.AlignCenter)
        self.title.setAlignment(Qt.AlignCenter)

        self.set_up_layout()

    # Sets up the layout of the GUI.
    def set_up_layout(self):
        widget = QWidget()

        self.setCentralWidget(widget)
        widget.setFixedHeight(600)
        widget.setFixedWidth(1000)

        timer_edit_layout = QGridLayout()
        timer_edit_layout.addWidget(self.hour_label, 0, 0)
        timer_edit_layout.addWidget(self.minute_label, 0, 1)
        timer_edit_layout.addWidget(self.second_label, 0, 2)
        timer_edit_layout.addWidget(self.hour_plus, 1, 0)
        timer_edit_layout.addWidget(self.hour_label2, 2, 0)
        timer_edit_layout.addWidget(self.hour_minus, 3, 0)
        timer_edit_layout.addWidget(self.minute_plus, 1, 1)
        timer_edit_layout.addWidget(self.minute_label2, 2, 1)
        timer_edit_layout.addWidget(self.minute_minus, 3, 1)
        timer_edit_layout.addWidget(self.second_plus, 1, 2)
        timer_edit_layout.addWidget(self.second_label2, 2, 2)
        timer_edit_layout.addWidget(self.second_minus, 3, 2)
        timer_edit_layout.addWidget(self.set_button, 4, 1)

        main_layout = QGridLayout()
        main_layout.addWidget(self.title, 0, 1)
        main_layout.addLayout(timer_edit_layout, 1, 1)
        main_layout.addWidget(self.time_label, 2, 1)
        main_layout.addWidget(self.timer_down_button, 3, 0)
        main_layout.addWidget(self.timer_up_button, 3, 2)

        main_layout.addWidget(self.start_button, 4, 0)
        main_layout.addWidget(self.pause_resume_button, 4, 1)
        main_layout.addWidget(self.reset_button, 4, 2)

        # Set height and width
        self.hour_plus.setFixedWidth(100)
        self.hour_label.setFixedWidth(100)
        self.hour_minus.setFixedWidth(100)
        self.minute_plus.setFixedWidth(100)
        self.minute_label.setFixedWidth(100)
        self.minute_minus.setFixedWidth(100)
        self.second_plus.setFixedWidth(100)
        self.second_label.setFixedWidth(100)
        self.second_minus.setFixedWidth(100)

        self.hour_label.setFixedWidth(100)
        self.minute_label.setFixedWidth(100)
        self.second_label.setFixedWidth(100)

        self.start_button.setFixedWidth(widget.width() // 3)
        self.pause_resume_button.setFixedWidth(widget.width() // 3)
        self.reset_button.setFixedWidth(widget.width() // 3)

        widget.setLayout(main_layout)

# Activates the timer.
    def timer_execute(self):
        self.qtime = QTimer()
        self.qtime.timeout.connect(self.timer_check)
        self.qtime.start(1000)

    # Checks if the timer has hit zero.
    def timer_check(self):
        if self.time_left < 1:
            self.qtime.stop()
            times_up()

        else:
            self.time_left = self.timer.count_down(self.time_left)
            self.reformat()

# Formats the timer.
    def reformat(self):
        self.my_format = self.timer.format_time(self.time_left)
        self.time_label.setText(self.my_format)

    # Change the time limit for the timer.
    def change_timer(self):
        self.time_left = self.timer.set_time(hours=self.chosen_hours,
                                             minutes=self.chosen_minutes,
                                             seconds=self.chosen_seconds)
        print(self.time_left)
        self.set_up_timer()

    # Format the time unit labels.
    def format_labels(self):
        hours = str(self.chosen_hours)
        minutes = str(self.chosen_minutes)
        seconds = str(self.chosen_seconds)

        if self.chosen_hours < 10:
            self.hour_label2.setText(f"0{hours}")
        else:
            self.hour_label2.setText(f"{hours}")

        if self.chosen_minutes < 10:
            self.minute_label2.setText(f"0{minutes}")
        else:
            self.minute_label2.setText(f"{minutes}")

        if self.chosen_seconds < 10:
            self.second_label2.setText(f"0{seconds}")
        else:
            self.second_label2.setText(f"{seconds}")

# Change time unit labels.
    def increase_hour_label(self):
        if self.chosen_hours == 99:
            self.chosen_hours = 0
        else:
            self.chosen_hours += 1
        self.format_labels()

    def decrease_hour_label(self):
        if self.chosen_hours == 0:
            self.chosen_hours = 99
        else:
            self.chosen_hours -= 1
        self.format_labels()

    def increase_minute_label(self):
        if self.chosen_minutes == 59:
            self.chosen_minutes = 0
        else:
            self.chosen_minutes += 1
        self.format_labels()

    def decrease_minute_label(self):
        if self.chosen_minutes == 0:
            self.chosen_minutes = 59
        else:
            self.chosen_minutes -= 1
        self.format_labels()

    def increase_second_label(self):
        if self.chosen_seconds == 59:
            self.chosen_seconds = 0
        else:
            self.chosen_seconds += 1
        self.format_labels()

    def decrease_second_label(self):
        if self.chosen_seconds == 0:
            self.chosen_seconds = 59
        else:
            self.chosen_seconds -= 1
        self.format_labels()

    # Changes the text of the hour label.
    def change_hour_label(self):
        max_hours = 99
        try:
            if int(self.hour_label2.text()) > max_hours:
                exceeded_time_limit(max_hours)
            else:
                self.chosen_hours = int(self.hour_label2.text())
                self.format_labels()
        except ValueError:
            print("Number must be an integer.")

    # Changes the text of the minute label.
    def change_minute_label(self):
        max_minutes = 59
        try:
            if int(self.minute_label2.text()) > max_minutes:
                exceeded_time_limit(max_minutes)
            else:
                self.chosen_minutes = int(self.minute_label2.text())
                self.format_labels()
        except ValueError:
            print("Number must be an integer.")

    # Changes the text of the second label.
    def change_second_label(self):
        max_seconds = 59
        try:
            if int(self.second_label2.text()) > max_seconds:
                exceeded_time_limit(max_seconds)
            else:
                self.chosen_seconds = int(self.second_label2.text())
                self.format_labels()
        except ValueError:
            print("Number must be an integer.")

# Feature methods
    # Starts the timer countdown.
    def start_timer(self):
        self.start_button.setEnabled(False)
        self.hour_plus.setEnabled(False)
        self.hour_minus.setEnabled(False)
        self.minute_plus.setEnabled(False)
        self.minute_minus.setEnabled(False)
        self.second_plus.setEnabled(False)
        self.second_minus.setEnabled(False)
        self.set_button.setEnabled(False)

        self.pause_resume_button.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.timer_up_button.setEnabled(True)
        self.timer_down_button.setEnabled(True)

        self.timer_execute()

# Pauses the timer
    def pause(self):
        self.qtime.stop()
        self.pause_resume_button.clicked.connect(self.resume)
        self.pause_resume_button.setText("Resume")

# Resumes timer countdown.
    def resume(self):
        self.timer_execute()
        self.pause_resume_button.clicked.connect(self.pause)
        self.pause_resume_button.setText("Pause")

    # Resets timer countdown, bringing it to the previously set time.
    def reset_timer(self):
        self.qtime.stop()
        self.time_left = self.timer.current_time_limit
        self.set_up_timer()

    # Enables and disable certain buttons in the timer.
    def set_up_timer(self):
        # Enable buttons
        self.start_button.setEnabled(True)
        self.hour_plus.setEnabled(True)
        self.hour_minus.setEnabled(True)
        self.minute_plus.setEnabled(True)
        self.minute_minus.setEnabled(True)
        self.second_plus.setEnabled(True)
        self.second_minus.setEnabled(True)
        self.set_button.setEnabled(True)

        # Change resume button functionality
        self.pause_resume_button.clicked.connect(self.pause)
        self.pause_resume_button.setText("Pause")

        # Disable buttons
        self.pause_resume_button.setEnabled(False)
        self.reset_button.setEnabled(False)
        self.timer_up_button.setEnabled(False)
        self.timer_down_button.setEnabled(False)
        self.reformat()

    # Adds 30 seconds to the timer.
    def add_time(self):
        if self.time_left > 359969:
            self.time_left = 359999
        else:
            self.time_left += 30
        self.reformat()

    # Takes 30 seconds away from the timer.
    def subtract_time(self):
        if self.time_left < 30:
            self.time_left = 0
        else:
            self.time_left -= 30

        self.reformat()


# Send a message that prompts you to enter a valid number.
def exceeded_time_limit(max_time_unit: int):
    time_unit_warning = QMessageBox()
    time_unit_warning.setGeometry(300, 300, 200, 200)
    time_unit_warning.setText(f"Please choose a whole integer between 0 and {max_time_unit}")
    time_unit_warning.exec_()


# Notify when the timer reaches zero
def times_up():
    time_alert = QMessageBox()
    time_alert.setGeometry(300, 300, 200, 200)
    time_alert.setText("Times up")
    time_alert.exec_()


def application():
    app = QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

application()

# if __name__ == "gui":
#     application()