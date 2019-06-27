import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute(
    'select * from employees'
)
rows = cursorObj.fetchall()
for row in rows:
    print(row)
con.commit()