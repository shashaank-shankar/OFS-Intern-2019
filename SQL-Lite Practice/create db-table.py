import sqlite3
con = sqlite3.connect('userdb.db')
cursorObj = con.cursor()

def selectTable (val):
    cursorObj.execute(
        "select " + val + " from user"
    )
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    con.commit()

def createTable ():
    cursorObj.execute(
        "create table user(userid integer primary key, username text)"
    )
    con.commit()
#createTable()
print("\n")
print("Create table:")
selectTable("*")
print("\n")

def insertTable (entities):
    cursorObj.executemany(
        'insert into user(userid, username) values(?,?)',entities
    )
    con.commit()
entities = [(1, "Shashaank"), (2, "Natalie"), (3, "Niyanth"), (4, "John"), (5, "Bob")]
#insertTable(entities)
print("Insert values:")
selectTable("*")
print("\n")

def updateTable ():
    cursorObj.execute(
        'update user set username = "Mark" where userid = 5'
    )
    con.commit()
#updateTable()
print("Update table:")
selectTable("*")
print("\n")

def deleteTable ():
    cursorObj.execute(
        'delete from user where userid = 4'
    )
    con.commit()
#deleteTable()
print("Delete one row:")
selectTable("*")