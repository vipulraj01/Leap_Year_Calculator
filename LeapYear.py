# This python program calculates leap year based on the user input of year
def is_leap(year):  #Defining a function called is_leap
    leap = False

    if year%4 == 0 and year %100 != 0:
        return True
    elif year%4 == 0 and year %100 == 0 and year%400 == 0:
        return True
    else:
        return leap  

year = int(input("Enter the year : "))  # Enter the Year which you have to check for leap year
print(is_leap(year))
