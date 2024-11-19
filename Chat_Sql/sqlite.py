import sqlite3


## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a ccursor object to insert record,create table
cursor=connection.cursor()

## Create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)


## Insert some more records

cursor.execute('''Insert into STUDENT values('Prince','Artificial intelligence','A',90)''')
cursor.execute('''Insert into STUDENT values('john','Data Science','B',70)''')
cursor.execute('''Insert into STUDENT values('Nilesh','Devops','C',80)''')
cursor.execute('''Insert into STUDENT values('Dipesh','Web Development','D',80)''')
cursor.execute('''Insert into STUDENT values('jacob','Machine Learning','E',85)''')


## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


## Commit your changes in the database
connection.commit()
connection.close()