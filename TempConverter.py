#print("\nThis program converts Celsius and Farenheit temperatures.")

def tempConvert (type, temperature):
    if type.upper() == "C":
        # convert to C
        new_temp = (temperature - 32.0) * (5.0/9.0)
        new_temp = round(new_temp, 2)
        #print("\n" + str(temperature) + "F is equal to " + str(new_temp) + "C.")
        return new_temp
    elif type.upper() == "F":
         # convert to F
        new_temp = (temperature * (9.0/5.0)) + 32.0
        new_temp = round(new_temp, 2.0)
        #print("\n" + str(temperature) + "C is equal to " + str(new_temp) + "F.")
        return new_temp


# repeats until 'C' or 'F' or 'E' is entered
# while True:
#     type_input = input("\nEnter 'C' to convert to Celsius\nEnter 'F' to convert to Farenheit\nEnter 'E' to Exit: ")
#     type_input = type_input.upper()
#     if type_input == "C":
#         temp_input = float(input("\nEnter a temperature in Farenheit: "))
#         tempConvert("C")
#     elif type_input == "F":
#         temp_input = float(input("\nEnter a temperature in Celsius: "))
#         tempConvert("F")
#     elif type_input == "E":
#         break   