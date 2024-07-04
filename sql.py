import sqlite3

connection = sqlite3.connect("student.db")

# create a cursor object to insert, create, retrive and so on

cursor = connection.cursor()

# create table

table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);


"""
cursor.execute(table_info)
#inserting records

cursor.execute('''Insert into STUDENT values('Solomon','CS','A',99)''')
cursor.execute('''Insert into STUDENT values('Abhilash','DS','B',87)''')
cursor.execute('''Insert into STUDENT values('Martin','AI','A',95)''')
cursor.execute('''Insert into STUDENT values('Mick','CS','B',50)''')
cursor.execute('''Insert into STUDENT values('Duck','DS','A',35)''')

#Display all records

print("The inserted records are ")

data = cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)

#close connection

connection.commit()
connection.close()