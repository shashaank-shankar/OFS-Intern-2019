# Write a Python script to display the various Date Time formats.
import time
import datetime
print('\n')
# a) Current date and time
print("Current date and time: " , datetime.datetime.now())
# b) Current year
print("Current Year: " , datetime.date.today().strftime("%Y"))
# c) Month of year
print("Current Month: " , datetime.date.today().strftime("%B"))
# d) Week number of the year
print("Current Week Number: " , datetime.date.today().strftime("%W"))
# e) Weekday of the week
print("Current Day of Week: " , datetime.date.today().strftime("%w"))
# f) Day of year
print("Current Day of Year: " , datetime.date.today().strftime("%j"))
# g) Day of the month
print("Current Day of Month: " , datetime.date.today().strftime("%d"))
# h) Day of week
print("Current Day of Week: " , datetime.date.today().strftime("%A"))
print('\n')