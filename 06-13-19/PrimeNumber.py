
while True:
    num = input("\nEnter 'E' to exit\nEnter a number above one to check if it's a prime number: ")
    if num.lower() == 'e':
        break
    elif num.isdigit() == False:
        print("Enter a number above 1!")
    elif int(num) <= 1:
        print("Enter a number above 1!")
    else:
        for val in range(2, int(num) + 1):
            # if test below doesn't pass its a prime num
            if val == int(num):
                print("\n"+str(num) + " is a prime number.\n")
                break
            # checks if remainder is 0
            elif int(num) % val == 0:
                print("\n"+str(num) + " isn't a prime number!\n")
                break
    