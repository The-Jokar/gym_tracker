import datetime as dt
import pandas as pd
import calendar as cal

class MonthlyCalender():
    def __init__(self):
        self.month = dt.datetime.now().month
        self.year = dt.datetime.now().year
        self.first_day, num_days = cal.monthrange(self.year, self.month)
        try:
            self.cal = pd.read_csv('calender.csv')
        except:
            self.cal = pd.DataFrame(index=range(1, 5), columns=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
            for j in range(0, 6):
                self.cal.loc[j] = " "
            week = 0
            for i in range(1, num_days + 1):
                day_of_week = (i + self.first_day - 1) % 7
                self.cal.iloc[week, day_of_week] = i
                if day_of_week == 6:
                    week += 1
        
    def __str__(self):
        return self.cal.to_string(index=False)

    def visit(self, visted):
        date = dt.datetime.now().day
        week = ((date + self.first_day) // 7)
        day_of_week = (date + self.first_day - 1) % 7
        if visted == 'yes':
            self.cal.iloc[week, day_of_week] = f"({date})"

        self.cal.to_csv('calender.csv', index=False)

cur_mnth = MonthlyCalender()
visit = input("Have you visited today? ")
cur_mnth.visit(visit)

print(cur_mnth)


