# Name: Ming Wei
# Course: CS 362
# Description: conditions for leap years
# Due: 1/30/2021

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")

