# magic methods are how you define how two objects of a custom class
# are compared to one another and how mathematical operations are
# performed on them

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # define how object is printed
    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    # define how two of the objects are added together
    def __add__(self, other_time):
        new_time = Time()
        new_sec = self.second + other_time.second
        new_min = self.minute + other_time.minute
        new_hr = self.hour + other_time.hour
        if new_sec >= 60:
            new_min += 1
            new_sec %= 60
        if new_min >= 60:
            new_hr += 1
            new_min %= 60
        new_hr %= 24
        
        new_time.hour = new_hr
        new_time.minute = new_min
        new_time.second = new_sec

        return new_time

def main():
    time1 = Time(1, 20, 30)
    print(time1)
    time2 = Time(23, 41, 30)
    print(time1 + time2)

main()