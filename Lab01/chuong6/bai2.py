import calendar
from datetime import date

#CauD-------------------------------------------------------------------------
def cauD():
    print("Câu D: Check Leap Year")
    currentYear = date.today().year
    leap = calendar.isleap(currentYear)
    print("Current Year:", currentYear)
    if (leap):
        print(f"The next leap year from {currentYear} is {currentYear + 4}")
    else:
        i = 0
        while i < 5:
            nextYear = currentYear + i
            if calendar.isleap(nextYear): 
                print(f"The next leap year from {currentYear} is {nextYear}") 
            i += 1
#cauD() #Uncomment this line to invoke the function

#CauE-------------------------------------------------------------------------
#print(dir(calendar)) #Uncomment this line to invoke the function

#CauF---------------------------------------
def cauF():
    print("Câu F: How many Leap Years between 2020 and 2050?")
    year = 2020
    count = 0
    while year <= 2050:
        if calendar.isleap(year):
            count += 1
        year += 1
    print(f"There are {count} leap years from 2020 to 2050")

#cauF() #Uncomment this line to invoke the function

#CauG-------------------------------------------------------------------------
weekday = calendar.weekday(2016,7,29)
#print(calendar.day_name[weekday]) #Uncomment this line to invoke the function