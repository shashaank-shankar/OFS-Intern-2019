import mysql.connector

IOTdb = mysql.connector.connect(
  host="iotplatform.c66jtrv2jovs.us-east-1.rds.amazonaws.com",
  user="iotplatformusr",
  passwd="iotplatformpwd",
  database ="temperature_data_logger"
)

cursorObj = IOTdb.cursor()

# 'columns' is what columns you want to select
# 'tablename' is the name of the table
def selectTable (columns, tablename):
    cursorObj.execute(
        "select " + columns + " from " + tablename
    )
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

selectTable("TEMPERATURE_READING", "RECORD_TEMPERATURE")
