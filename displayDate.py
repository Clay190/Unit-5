#Clay Kynor
#11/15/17
#displayDate.py

import datetime

months = ['January', 'February', "March", 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekday = ['Monday', 'Tuesday', 'Wensday', 'Thursday', 'Firday', 'Saturday', 'Sunday']
today = datetime.date.today()
day = today.day
month = today.month
year = today.year

print(month, day, year)
