# Name: Ming Wei
# Course: CS 362
# Description: conditions for leap years with error handling
# Due: 1/15/2021

# To get year (integer input) from the user
while True:
    try:
        year = int(input("Enter a year: "))
        year = int(year)
    except:
        year = int(input("Input error, Enter a year: "))
    else:
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            print(year, "is a leap year!")
        else:
            print(year, "is not a leap year!")
        break
