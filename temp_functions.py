import mysql.connector

# Connects this file to Temperature Database
IOTdb = mysql.connector.connect(
  host="iotplatform.c66jtrv2jovs.us-east-1.rds.amazonaws.com",
  user="iotplatformusr",
  passwd="iotplatformpwd",
  database ="temperature_data_logger"
)

# What allows Python to execute SQL queries
cursorObj = IOTdb.cursor()

# List of all values from a column (EX: Decimal('89.00'))
column_values = []
# List of all isolated values from a column (EX: '89.00')
column_values_iso = []

# 'tablename' is the name of the table
# 'column_num' is the number of the column that is selected
# 'list' is the list the values are appended to
def selectTable (tablename, column_num, list):
    cursorObj.execute(
        "select * from " + tablename
    )
    records = cursorObj.fetchall()
    for row in records:
        list.append(row[column_num])
    IOTdb.commit()

# Adds all values from 'RECORD_TEMPERAURE' to column_values
selectTable("RECORD_TEMPERATURE", 2, column_values)

# Isolates value from 'list'
# Appends value to 'list_append'
def value_strip (list, list_append):
    for value in list:
        value = str(value)
        value.strip()
        list_append.append(value)

# Isolates temperature from 'column_values' and appends to 'column_values_iso'
value_strip(column_values, column_values_iso)

# Converts temperature to either F or C
def tempConvert (type, temperature):
    if type.upper() == "C":
        # Converts temperature to C
        new_temp = (temperature - 32.0) * (5.0/9.0)
        new_temp = round(new_temp, 2)
        return new_temp
    elif type.upper() == "F":
         # Converts temperature to F
        new_temp = (temperature * (9.0/5.0)) + 32.0
        new_temp = round(new_temp, 2.0)
        return new_temp

# Returns average of values in 'list'
def average (list):
    sum = 0
    count = 0
    for value in list:
        sum = sum + float(value)
        count += 1
    average = round(sum/count, 2)
    return average

# Prints average temperature of 'columns_values_iso' in F and C
print("\nAVERAGE:")
print("The average is "+ str(average(column_values_iso)) + " degrees Farenheit")
print("and " + str(tempConvert('c', average(column_values_iso))) + " degrees Celsius.")

#Find the min value
def min_function(list):
    min_value = None
    for value in list:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

# Prints the minimum temperature of 'columns_values_iso' in F and C
print("\nMINIMUM:")
print("The minimum temperature is " + min_function(column_values_iso) + " degrees Farenheit")
print("and " + str(tempConvert('c', float(min_function(column_values_iso)))) + " degrees Celsius.\n")

# Find the max value
def max_function(list):
    max_value = None
    for value in list:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    return max_value

# Prints the maximum temperature of 'columns_values_iso' in F and C
print('\nMAXIMUM:')
print("The minimum temperature is " + max_function(column_values_iso) + " degrees Farenheit")
print("and " + str(tempConvert('c', float(max_function(column_values_iso)))) + " degrees Celsius.\n")
