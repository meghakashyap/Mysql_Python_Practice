import mysql.connector

# HERE WE ARE ACONNECTING
mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='Megha@8287',
    database='CLASS_WITH_MEGHA'
)

# create cursor
mycursor = mydb.cursor()

# Create DATABASE
# mycursor.execute('CREATE DATABASE CLASS_WITH_MEGHA') 

# create tables
# mycursor.execute('CREATE TABLE DATA (ID integer,NAME varchar(50), AGE integer)')

# mycursor.execute('DESC DATA')
# for i in mycursor:
#     print(i)

# data insert
# sql = 'INSERT INTO DATA(ID,NAME,AGE) VALUES(%s,%s,%s)'
# val = [
#     (1,'Megha',20),
#     (2,'Neha',22),
#     (3,'Mamatha',22),
#     (4,'bhaga',19)
# ]
# mycursor.executemany(sql,val)

# mydb.commit()


# mycursor.execute('SELECT * FROM DATA')
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)      
         
                                                                                                                                                                                    
# 2NDTABLE                                                                                
# mycursor.execute('CREATE TABLE INFO (ID integer,NAME varchar(50), YEAR integer)')
# data insert
# sql = 'INSERT INTO INFO(ID,NAME,YEAR) VALUES(%s,%s,%s)'
# val = [
#     (1,'Megha',2001),
#     (2,'Neha',1999),
#     (3,'Mamatha',1999),
#     (4,'bhaga',2002),
#     (5,"x",1995)
# ]
# mycursor.executemany(sql,val)

# mydb.commit()

# JOINING TWO TABLE
value = 'SELECT INFO.ID,INFO.NAME \
        FROM DATA LEFT JOIN INFO ON INFO.ID=DATA.ID'
mycursor.execute(value)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)      
         
         
 
# INFO =5(L)
# DATA =4(R)