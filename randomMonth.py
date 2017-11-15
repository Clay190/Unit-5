#Clay Kynor
#11/13/17
#randomMonth.py - random month of the year

from random import randint

months = ['January', 'February', "March", 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num = randint(1,12)
print(months[num])