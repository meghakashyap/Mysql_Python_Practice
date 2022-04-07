import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Megha@8287',
    database = 'demo'
)

mycursor = mydb.cursor()

# # Creating Table
# mycursor.execute('CREATE TABLE Managers (EMPNO integer,ENAME Varchar(30),JOB varchar(50),DEPTNO integer,MGR integer)')

# # Insert many Data in table 
# sql  = "INSERT INTO Managers (EMPNO,EName,JOB,DEPTNO,MGR) VALUES(%s ,%s, %s,%s,%s)"
# val = [(7839,"Megha","PRESIDENT",10,7839),
#        (7698,"Bharti","MANAGER",30,7839),
#        (7782,"Sheetal","Commerce",10,7839),
#        (7566,"Suvarna","Arts",20,7698)
#        ]

# # we are using executemany for inserting more than one rows
# mycursor.executemany(sql,val)

# # commiting changes
# mydb.commit()

mycursor.execute('SELECT * FROM Managers WHERE EMPNO  != MGR')
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
