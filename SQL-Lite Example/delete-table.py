import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute(
    'delete from employees where id=2'
)

con.commit()