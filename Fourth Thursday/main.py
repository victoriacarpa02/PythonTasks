import calendar
from datetime import date


class FourthThursday:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.date = calendar.monthcalendar(year, month)

    @property
    def right_day(self):
        if self.date[0][3] != 0:
            return date(self.year, self.month, self.date[3][3])
        return date(self.year, self.month, self.date[4][3])

    def __str__(self):
        return self.right_day.strftime('%d.%m.%Y')


user_input = FourthThursday(int(input()), int(input()))
print(user_input)

