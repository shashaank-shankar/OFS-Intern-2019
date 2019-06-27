import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute(
    'update employees set firstname = "Niyanth" where id = 3'
)
con.commit()