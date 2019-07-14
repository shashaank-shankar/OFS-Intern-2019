import TempConverter
import mysql.connector

# connects file to database
IOTdb = mysql.connector.connect(
  host="iotplatform.c66jtrv2jovs.us-east-1.rds.amazonaws.com",
  user="iotplatformusr",
  passwd="iotplatformpwd",
  database ="temperature_data_logger"
)

cursorObj = IOTdb.cursor()

# list of all temperatures recorded
temperature_list_temp = []
# list w/ isolated numbers
temperature_list = []

# 'columns' is what columns you want to select
# 'tablename' is the name of the table
def selectTable (columns, tablename):
    cursorObj.execute(
        "select " + columns + " from " + tablename
    )
    records = cursorObj.fetchall()
    #rows = list(records)
    #print(records)
    for row in records:
        temperature_list_temp.append(row[2])
        #print(row)
    IOTdb.commit()

# isolates number from entry
def temperaturelist_strip (list):
    for value in list:
        value = str(value)
        value.strip()
        #print(value)
        temperature_list.append(value)

# gets average of list
def average (list):
    sum = 0
    count = 0
    for value in list:
        sum = sum + float(value)
        count += 1
    average = round(sum/count, 2)
    return average

# converts temperature
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

# adds all values to temperature_list_temp
selectTable("*", "RECORD_TEMPERATURE")

# isolates number
temperaturelist_strip(temperature_list_temp)

print("The average is "+ str(average(temperature_list)) + " degrees Farenheit.")
print("It is also " + str(tempConvert('c', average(temperature_list))) + " degrees Celsius.")