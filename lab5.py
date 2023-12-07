"""Module error"""


class TimeConverter:
    """
    Main function
    """
    def __init__(self, _time: str, hours=None, minutes=None, seconds=None):
        try:
            _hours, _minutes, _seconds = _time.split(":")
            self.hours = int(_hours)
            self.minutes = int(_minutes)
            self.seconds = int(_seconds)
        except ValueError:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def time_to_seconds(self):
        """
        Turns time in format hh:mm:ss into seconds
        :return:
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, total_seconds):
        """
        Turns seconds into a time, formatted as hh:mm:ss
        :param total_seconds:
        :return:
        """
        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def output_converted_time(self, time_format='hh:mm:ss'):
        """
        Gives an output, which differs with different inputs.
        Accepts either numbers or time in format hh:mm:ss
        :param time_format:
        :return:
        """
        if time_format == 'hh:mm:ss':
            print(str(self))
        elif time_format == 'seconds':
            print(f"Total seconds: {self.time_to_seconds()}")
        else:
            print("Invalid time format. Supported formats: 'hh:mm:ss', 'seconds'")


if __name__ == "__main__":
    time_converter = TimeConverter("", hours=0, minutes=0, seconds=45)
    time_converter2 = TimeConverter("22:10:30")

    time_converter3 = TimeConverter("aswda:10:30")
    time_converter.output_converted_time(time_format='seconds')

    time_converter2.output_converted_time(time_format='seconds')
    time_converter.seconds_to_time(9000)
    time_converter.output_converted_time()
    time_converter2.seconds_to_time(3456)
    time_converter2.output_converted_time()
