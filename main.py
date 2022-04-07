
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='Megha@8287',
  database ="demo"
)

myacces = mydb.cursor()

# Creating database
# myacces.execute("CREATE DATABASE PYTHON_PROJECT")

# deleting database
# myacces.execute("DROP DATABASE PYTHON_PROJECT")

# show databases
# myacces.execute("SHOW DATABASES")
# for database in myacces:
#     print(database)

# Creating table
# myacces.execute("CREATE TABLE  Students (Id integer, Name VARCHAR(255), Stream VARCHAR(255))")


# Show tables
# myacces.execute("SHOW TABLES")
# for table in myacces:
#     print(table)
    
# Insert one value Data 
sql  = "INSERT INTO Students (Id,Name,Stream) VALUES(%s ,%s, %s)"
val =(1,"Megha","Science")
myacces.execute(sql,val)


# Insert many Data in table 
# sql  = "INSERT INTO Students (Id,Name,Stream) VALUES(%s ,%s, %s)"
# val = [(1,"Megha","Science"),
#        (2,"Bharti","Commerce"),
#        (3,"Sheetal","Commerce"),
#        (4,"Suvarna","Arts")
#        ]

# # we are using executemany for inserting more than one rows
# myacces.executemany(sql,val)

# # commiting changes
# mydb.commit()
# print(myacces.rowcount,"record inserted")

# describing the table
# myacces.execute('DESC Students')
# for x in myacces:
#     print(x)
    
# myacces.execute('SELECT Id,Name FROM Students ')
# We use the fetchall() method, which fetches all rows from the last executed statement.
result = myacces.fetchall() 
# for i in result:
#     print(i)

# using Like for filterning the records
myacces.execute("SELECT * FROM Students WHERE Name LIKE '%a'")
myresult = myacces.fetchall()
for x in myresult:
  print(x)


# FWS (From,Where,Select)- Order of Execution in SQL






# If you are only interested in one row, you can use the fetchone() method.
# The fetchone() method will return the first row of the result:
# myresult = myacces.fetchone()
# print(myresult)