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

def average (list):
    sum = 0
    count = 0
    for value in list:
        sum = sum + float(value)
        count += 1
    average = round(sum/count, 2)
    return average

def temperaturelist_strip (list):
    for value in list:
        value = str(value)
        value.strip()
        #print(value)
        temperature_list.append(value)

selectTable("*", "RECORD_TEMPERATURE")

# isolates number
temperaturelist_strip(temperature_list_temp)

print("The average is "+ str(average(temperature_list)) + " degrees Farenheit.")
