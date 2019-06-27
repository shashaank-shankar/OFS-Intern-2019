import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute(
    "Create table employees(id integer primary key, firstname text, lastname text)"
)
con.commit()