import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
entities = (3, 'Bob', 'Ross')
cursorObj.execute(
    'insert into employees(id, firstname, lastname) values(?,?,?)',entities
)
con.commit()
