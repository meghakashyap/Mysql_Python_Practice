import mysql.connector

# creating connection between python and mysql database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Megha@8287",
    database = "PAYROLL_SYSTEM"
)

# Creating cursor
mycursor = mydb.cursor()

# Creating database
mycursor.execute('CREATE DATABASE PAYROLL_SYSTEM')

# Creating Employee Table
mycursor.execute('CREATE TABLE EMPLOYEE (EMP_ID integer, FIRSTNAME varchar(50),LASTNAME varchar(50),PHONENO integer,AGE integer,EMAIL varchar(50),EMP_MANAGER varchar(50),ADDRESS varchar(50))')

# ADDING NEW COLUMN INTO EMPLOYEE TABLE
mycursor.execute('ALTER TABLE EMPLOYEE ADD (BLOOD_GROUP CHAR(20),GENDER CHAR(8),DESIGNATION CHAR(20),YEARS_OF_WORKING integer)')

# DESCRIBING TABLE ENTITIES
mycursor.execute('DESC EMPLOYEE')
for i in mycursor:
    print(i)

# INSERTING DATA INTO EMPLOYEE TABLE
sql = 'INSERT INTO EMPLOYEE (EMP_ID,FIRSTNAME,LASTNAME,PHONENO,AGE,EMAIL,Emp_Manager,ADDRESS,BLOOD_GROUP,GENDER,DESIGNATION,YEARS_OF_WORKING) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val = [
    (101,'Jack','Beneath',98765123,29,'jackbean29@gmail.com','Rakesh Sharma','6/63 B blok London','AB+','Male','Full Stack Devloper',8),
    (102,'Stefan','Cooper',87561723,23,'stefancooper@gmail.com','Megha','JJ colony Badarpur','O+','Male','Back-End Devloper',4),
(103,'Elena','Gilbert',88976543,22,'elenagilbert@gmail.com','Ravishankar','London','AB+','Female','Frontend Devloper',3),
(104,'Bonny','Beneth',98765432,24,'bonbon@gmail.com','Umang','Sarita vihar Delhi','B+','Female','Frontend Devloper',5),
(105,'Matt','Simeton',76543452,32,'mattbeneth@gmail.com','Umang','Lajpat nagar Delhi','B-','Male','Full StacK Devloper',12),
(106,'Calorine','Forbes',98543452,23,'calorine@gmail.com','Ananat','Delhi,NewDelhi',')+','Female','Back-End Devloper',5),
(107,'Alaric','Jackson',8943456,26,'alaricjackson@gmail.com','Supriya','2/12 Old Faridabad','AB-','Male','Full Stack Devloper',7),
(108,'Megha','Kashyap',82877836,20,'meghakashyap20@gmail.com','Ravishankar','SriNiwasPuri Delhi','O+','Female','Backend-Devloper',1),
(109,'Raghav','Pandey',76828799,22,'raghavpandey@gmail.com','Supriya','Rajori garden,Delhi','B+','Male','Full Stack Devloper',3),
(110,'Vivek','Chauhan',88728799,24,'vivekchauhan@gmail.com','Ravishankar','SEctor-10,Noida','AB+','Male','Backend Devloper',5)
]
mycursor.executemany(sql,val)
mydb.commit()

# SELECTING DATA FORM EMPLOYEE TABLE
mycursor.execute('SELECT * FROM EMPLOYEE')
for rows in mycursor:
    print(rows)


# Creating Department Table
mycursor.execute('CREATE TABLE DEPARTMENT (DEPTNO CHAR(3) NOT NULL,EMP_ID integer,DEPTNAME  VARCHAR(36)  NOT NULL,MGRNO  CHAR(6) ,DEP_STATUS varchar(5) ,LOCATION  CHAR(50))')

# DESCRIBING DEPARTMENT TABLE
mycursor.execute('DESC DEPARTMENT')
for rows in mycursor:
    print(rows)

# INSERTING DATA INTO DEPARTMENT TABLE
sql = 'INSERT INTO DEPARTMENT(DEPTNO,EMP_ID,DEPTNAME,MGRNO,DEP_STATUS,LOCATION) VALUES (%s,%s,%s,%s,%s,%s)'
val = [
    ('SD0',101,'DATA ANALYST','FS101','ON','LONDON,UK'),
    ('BD1',102,'DEVOPS','BD102','ON','DELHI'),
    ('FD2',103,'API','FD103','ON','LONDON,UK'),
    ('FD2',104,'API','FD104','ON','GURUGRAM'),
    ('SD0',105,'DEVOPS','FS105','ON','DELHI'),
    ('BD1',106,'DATA ANALYST','BD106','ON','GURUGRAM'),
    ('SD0',107,'DATA ANALYST','FS107','ON','GURUGRAM'),
    ('BD1',108,'DATA SCIENCE','BD108','ON','DELHI'),
    ('SD0',109,'DEVOPS','FS109','ON','DELHI'),
    ('BD1',110,'DATA ANALYST','BD110','ON','DELHI')
]

mycursor.executemany(sql,val)
mydb.commit()

# SELECTING DATA FORM DEPARTMENT TABLE
mycursor.execute('SELECT * FROM DEPARTMENT')
for rows in mycursor:
    print(rows)




# DESCRIBING DEPARTMENT TABLE
mycursor.execute('DESC PAYROLL')
for rows in mycursor:
    print(rows)


# Creating PAYROLL Table
mycursor.execute('CREATE TABLE PAYROLL(EMP_ID integer,DEPNO CHAR(3),SALARY integer ,TAX integer,TOTAL_SALARY integer)')

# INSERT DATA INTO PAYROLL
sql = 'INSERT INTO PAYROLL (EMP_ID,DEPNO,SALARY,TAX,TOTAL_SALARY) VALUES(%s,%s,%s,%s,%s)'
val = [
    (101,'SD0',40000,2,0),
    (102,'BD1',45000,3,0),
    (103,'FD2',20000,1,0),
    (104,'FD2',30000,1,0),
    (105,'SD0',430000,2,0),
    (106,'BD1',20000,1,0),
    (107,'SD0',24000,2,0),
    (108,'BD1',40000,2,0),
    (109,'SD0',500000,3,0),
    (110,'BD1',10000,0,0)
    
]
mycursor.executemany(sql,val)
mydb.commit()

#  SELECTING DATA FORM PAYROLL TABLE
mycursor.execute('SELECT * FROM PAYROLL')
for rows in mycursor:
    print(rows)



# Creating EMP_STATUS Table
mycursor.execute('CREATE TABLE EMP_STATUS(EMP_ID integer,IN_TIME TIME,OUT_TIME TIME,JOINING_DATE DATE, PROMOTION CHAR(10),ACTIVE_STATUS CHAR(5),VACCINATION CHAR(10))')


# DESCRIBING EMP_STATUS TABLE
mycursor.execute('DESC EMP_STATUS')
for rows in mycursor:
    print(rows)


# INSERTING DATA INTO EMP_STATUS
sql = 'INSERT INTO EMP_STATUS(EMP_ID,IN_TIME,OUT_TIME,JOINING_DATE,PROMOTION,ACTIVE_STATUS,VACCINATION) VALUES(%s,%s,%s,%s,%s,%s,%s)'
val = [
    (101,'9:00:00','6:30:00','2016-04-16','YES','YES','COMPLETED'),
    (102,'9:00:00','6:30:00','2016-04-16','YES','YES','COMPLETED'),
    (103,'9:00:00','6:30:00','2019-01-17','YES','YES','ONE LET'),
    (104,'9:00:00','6:30:00','2020-03-12','N0','YES','COMPLETED'),
    (105,'9:00:00','6:30:00','2010-08-29','YES','NO','PENDING'),
    (106,'9:00:00','6:30:00','2018-02-12','NO','YES','COMPLETED'),
    (107,'9:00:00','6:30:00','2015-03-16','YES','YES','PENDING'),
    (108,'9:00:00','6:30:00','2021-03-05','NO','YES','COMPLETED'),
    (109,'9:00:00','6:30:00','2020-02-24','NO','NO','ONE LEFT'),
    (110,'9:00:00','6:30:00','2018-01-01','YES','YES','COMPLETED')
]
mycursor.executemany(sql,val)
mydb.commit()
    
#  SELECTING DATA FORM EMP_STATUS TABLE
mycursor.execute('SELECT * FROM EMP_STATUS')
for rows in mycursor:
    print(rows)

# CREATING ATTENDANCE TABLE
mycursor.execute('CREATE TABLE ATTENDANCE(EMP_ID INTEGER NOT NULL, LEAVES INTEGER NOT NULL, DAY_ATTENTED INTEGER NOT NULL)')


# DESCRIBING ATTENDANCE TABLE
mycursor.execute('DESC ATTENDANCE')
for rows in mycursor:
    print(rows)

# INSERTING DATA IN ATTENDANCE TABLE
sql = 'INSERT INTO ATTENDANCE (EMP_ID,LEAVES,DAY_ATTENTED) VALUES(%s,%s,%s)'
val = [
    (101,2,24),
    (102,0,26),
    (103,5,21),
    (104,2,24),
    (105,1,25),
    (106,0,26),
    (107,15,11),
    (107,2,24),
    (109,3,23),
    (110,0,26)
]
mycursor.executemany(sql,val)
mydb.commit()

#  SELECTING DATA FORM ATTENDANCE TABLE
mycursor.execute('SELECT * FROM ATTENDANCE')
for rows in mycursor:
    print(rows)


# UPDATING TOTAL_SALAY FROM PAYROLL TABLE
sql ='UPDATE PAYROLL SET TOTAL_SALARY = CASE WHEN SALARY > 30000 THEN SALARY*100/2 ELSE 35000 END'
mycursor.execute(sql)
mydb.commit()


# deleting ROW from attendance table
sql = "DELETE FROM ATTENDANCE WHERE EMP_ID = 110"
mycursor.execute(sql)
mydb.commit()


# Updating the name from EMPLOYEE table
sql = 'UPDATE EMPLOYEE SET FIRSTNAME = "Shivansh" WHERE EMP_ID = 101'
mycursor.execute(sql)
mydb.commit()

# fetching the data
mycursor.execute('SELECT * FROM EMPLOYEE')
myresult = mycursor.fetchall()
for x in myresult:
  print(x)      

# INCREASING THE SALARY 
sql = 'SELECT EMPLOYEE.EMP_ID,FIRSTNAME,YEARS_OF_WORKING,SALARY,\
    CASE WHEN EMPLOYEE.YEARS_OF_WORKING>5 THEN  SALARY+2000 \
    ELSE SALARY+1000 END AS PROMOTION_SALARY FROM EMPLOYEE\
    INNER JOIN  PAYROLL ON PAYROLL.EMP_ID=EMPLOYEE.EMP_ID'
    
mycursor.execute(sql)
for i in mycursor:
    print(i)

   