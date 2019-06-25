
while True:
    upper = 1000
    count = 0
    num1 = 0
    num2 = 1
    limit = input("\nEnter 'E' to Exit\nEnter a number to display\nFibonacci Sequence up to that number: ")
    if limit.lower() == 'e':
        break
    elif limit.isdigit() == False:
        print("Enter only numbers above 0!")
    else:
        if int(limit) <= 0:
            print("\nEnter a postive number!")
        elif int(limit) >= upper:
            print("Enter a number smaller than 1000!")
        else:
            if int(limit) == 1:
                print("\nThe Fibonacci Sequence for " + str(limit) + " is:")
                print(num1)
            else:
                print("\nThe Fibonacci Sequence for " + str(limit) + " is:")
                while count < int(limit):
                    print(str(num1))
                    temp_num = num1 + num2
                    num1 = num2
                    num2 = temp_num
                    count += 1
