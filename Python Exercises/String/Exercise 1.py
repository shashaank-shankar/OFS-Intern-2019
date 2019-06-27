# Write a Python program to calculate the length of a string

a = input("Enter: ")
count = 0
for char in a:
    count += 1
print("The length of " + a + " is " + str(count) + " characters.")