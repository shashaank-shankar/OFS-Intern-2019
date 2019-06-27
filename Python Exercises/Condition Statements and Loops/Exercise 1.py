# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

input = int(input("Enter a number: "))
if input >= 1500 and input <= 2700:
    if input%7 == 0:
        if input%5 == 0:
            print(input + " is between 1500 and 2700. It is also divisable by 7 and 5.")
