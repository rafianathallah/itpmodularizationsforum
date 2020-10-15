import calendar

def exactdate(year, month):
    date = calendar.TextCalendar(firstweekday=0)
    print(date.formatmonth(year, month, 0, 1))

exactdate(2002, 3)
    
    