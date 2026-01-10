class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = Clock.time_rollover(hour, minute)

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}({self.hour!r}, {self.minute!r})'

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return (self.hour == other.hour and self.minute == other.minute)

    def __add__(self, minutes):
        hours, minutes = Clock.get_hm(minutes)
        new_hours = self.hour + hours 
        new_minutes = self.minute + minutes 
        return Clock(new_hours, new_minutes)

    def __sub__(self, minutes):
        hours, minutes = Clock.get_hm(minutes)
        new_minutes = self.minute - minutes 
        if new_minutes < 0:
            new_minutes += 60
            new_hours = self.hour - hours - 1
        else: 
            new_hours = self.hour - hours
        if new_hours < 0:
            new_hours += 24
        return Clock(new_hours, new_minutes)

    @staticmethod
    def get_hm(mins):
        hours = (mins//60) % 24
        minutes = mins % 60
        return hours, minutes
    
    @staticmethod
    def time_rollover(hour, minute):
        hours = hour % 24
        extra_hours, minutes = Clock.get_hm(minute)
        hours += extra_hours
        if hours >= 24:
            hours -= 24
        return hours, minutes