# 5/19/25 Created a timer format.
# Next time, Try to get the format on PyQt5
import time

second_test = 3


class Timer:
    def __init__(self):
        self.current_time_limit = 0

    def format_time(self, seconds):
        second_format = f"{seconds % 60}"
        minute_format = f"{seconds // 60 % 60}"
        hour_format = f"{seconds // 3600}"

        if int(hour_format) < 10:
            hour_format = f"0{hour_format}"

        if int(minute_format) < 10:
            minute_format = f"0{minute_format}"

        if int(second_format) < 10:
            second_format = f"0{second_format}"

        # self.time_format = f"{hour_format}:{minute_format}:{second_format}"
        return f"{hour_format}:{minute_format}:{second_format}"


    def count_down(self, num_of_seconds):
        if num_of_seconds > 0:
            num_of_seconds -= 1
        return num_of_seconds


    def set_time(self, hours:int, minutes:int, seconds:int):
        number_of_seconds = 0
        number_of_seconds += (hours * 3600)
        number_of_seconds += (minutes * 60)
        number_of_seconds += seconds
        self.current_time_limit = number_of_seconds
        return number_of_seconds





# timer(183)



