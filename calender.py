import datetime as dt
import pandas as pd
import calendar as cal

class MonthlyCalender():
    """
    This class generates or reads a monthly calender and allows the user to mark the days they have visited the gym.
    """ 
    def __init__(self):
        """
        Initialises the calender with the current month and year or reads the existing calender all using pandas to read csv
        and data frames to store calendar data.

        time complexity: O(1) all operations are done in constant time and for loops have a fixed number of iterations
        space complexity: O(1) array size will always be fixed at 6x7
        """
        # initialise class variables
        self.month = dt.datetime.now().month
        self.year = dt.datetime.now().year
        self.first_day, num_days = cal.monthrange(self.year, self.month)
        # check for an exisiting calendar if not create a new one
        try:
            self.cal = pd.read_csv('calender.csv')
        except:
            # create a data frame to store the calender
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
        """
        Prints the calendar as a string

        time complexity: O(1) all operations are done in constant time
        space complexity: O(1) does not generate any new data
        """
        return self.cal.to_string(index=False)

    def visit(self, visted):
        """
        Updates the calendar based on if you visited the gym or not

        time complexity: O(1) all operations are done in constant time
        space complexity: O(1) does not generate any new data only updates exiuisting data
        """
        date = dt.datetime.now().day
        week = ((date + self.first_day) // 7)
        day_of_week = (date + self.first_day - 1) % 7
        # if visited update the data frame and write to csv
        if visted == 'yes':
            self.cal.iloc[week, day_of_week] = f"({date})"

        self.cal.to_csv('calender.csv', index=False)


