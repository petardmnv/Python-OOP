class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds += 1
        if self.seconds >= Time.max_seconds:
            self.seconds = 00
            self.minutes += 1
            if self.minutes >= Time.max_minutes:
                self.minutes = 00
                self.hours += 1
            if self.hours >= Time.max_hours:
                self.hours = 00

        return self.get_time()


time = Time(9, 30, 59)

print(time.next_second())

time1 = Time(10, 59, 59)

print(time1.next_second())

time2 = Time(23, 59, 59)

print(time2.next_second())
print(time2.next_second())

