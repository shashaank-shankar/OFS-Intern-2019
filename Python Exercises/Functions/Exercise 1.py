# Write a Python function to find the Max of three numbers

def max(num1, num2, num3):
    print("The biggest number is:")
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

max(input("Enter a number:"), input("Enter a number:"), input("Enter a number:"))