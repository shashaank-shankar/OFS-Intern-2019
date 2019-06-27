# Write a Python program to convert temperatures to and from celsius, fahrenheit.
print("\nThis program converts Celsius and Farenheit temperatures.")

def tempConvert (type):
    if type == "C":
        # convert to C
        new_temp = (temp_input - 32) * (5/9)
        new_temp = round(new_temp, 2)
        print("\n" + str(temp_input) + "F is equal to " + str(new_temp) + "C.")
    elif type == "F":
         # convert to F
        new_temp = (temp_input * (9/5)) + 32
        new_temp = round(new_temp, 2)
        print("\n" + str(temp_input) + "C is equal to " + str(new_temp) + "F.")

# repeats until 'C' or 'F' is entered
while True:
    type_input = input("\nEnter 'C' to convert to Celsius\nEnter 'F' to convert to Farenheit\nEnter 'E' to Exit: ")
    type_input = type_input.upper()
    if type_input == "C":
        temp_input = float(input("\nEnter a temperature in Farenheit: "))
        tempConvert("C")
    elif type_input == "F":
        temp_input = float(input("\nEnter a temperature in Celsius: "))
        tempConvert("F")
    elif type_input == "E":
        break   