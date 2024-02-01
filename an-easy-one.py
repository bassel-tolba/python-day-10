
def is_leap(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



def days_in_month(year, month):
    """returns the number of days a certain month has"""
    year = int(year)
    month = int(month) - 1
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        month_days[1] = 29
        
    elif is_leap(year) == False:
        month_days[1] = 28

    return month_days[month]

year = int(input("what is the year ?"))
month = int(input("what is the month ?"))
print(days_in_month(year, month))