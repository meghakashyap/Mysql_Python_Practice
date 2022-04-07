import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Megha@8287',
    database =  'RESTAURANT_MANAGMENT'
)

# creating cursor
myacces = mydb.cursor()

#creating database
myacces.execute('CREATE DATABASE RESTAURANT_MANAGMENT')

#Creating table restaurant managment
myacces.execute('CREATE TABLE ORDERS (CUST_ID integer NOT NULL,ITEM_ID integer NOT NULL,QUANTITY integer NOT NULL,UNIT_COST integer NOT  NULL,SUB_TOTAL integer NOT NULL)')

# DESCRIBING ORDERS TABLE
myacces.execute('DESC ORDERS')
for rows in myacces:
    print(rows)

# inserting data into orders tabel
sql = 'INSERT INTO ORDERS(CUST_ID,ITEM_ID,QUANTITY,UNIT_COST,SUB_TOTAL) VALUES(%s,%s,%s,%s,%s)'
val = [
    (811,902,2,250,2*250),
    (811,901,1,100,1*100),
    (815,904,3,350,3*350),
    (815,910,1,150,1*150),
    (814,909,5,90,5*90),
    (812,907,1,150,1*150),
    (812,902,1,250,1*250),
    (812,904,1,350,1*350)
]
myacces.executemany(sql,val)
mydb.commit()

myacces.execute('SELECT * FROM ORDERS')
for rows in myacces:
    print(rows)

# Creating table inside restaurant managment
myacces.execute('CREATE TABLE CUSTOMER(CUST_ID integer NOT NULL,NAME CHAR(30) NOT NULL,PHONENO integer NOT NULL,LOCATION CHAR(50) NOT NULL, ZIPCODE integer NOT NULL)')

# DESCRIBING CUSTOMER TABLE
myacces.execute('DESC CUSTOMER')
for rows in myacces:
    print(rows)
    
# INSERTING DATA 
sql = 'INSERT  INTO CUSTOMER(CUST_ID,NAME,PHONENO,LOCATION,ZIPCODE) VALUES(%s,%s,%s,%s,%s)'
val = [
    (811,'Raghav',878200,'Lajpat Nagar',10065),
    (812,'Megha',958360,'Rajori Garden',10035),
    (813,'Abhay',782385,'Uttam Nagar',10023),
    (814,'Neha',658360,'Nehru Place',10013),
    (815,'Bharti',758360,'Sarita vihar',10015)
]
myacces.executemany(sql,val)
# commiting the change in database
mydb.commit()

#  SELECTING DATA FORM CUSTOMER TABLE
myacces.execute('SELECT * FROM CUSTOMER')
for rows in myacces:
    print(rows)



# Creating MENU TABLE
myacces.execute('CREATE TABLE MENU(ITEM_ID integer NOT NULL,ITEM_NAME CHAR(50),PRICE integer NOT NULL,TYPE CHAR(30),CATEGORY CHAR(50))')

# DESCRIBING CUSTOMER TABLE
myacces.execute('DESC MENU')
for rows in myacces:
    print(rows)

    
# INSERTING DATA 
sql = 'INSERT  INTO MENU(ITEM_ID,ITEM_NAME,PRICE,TYPE,CATEGORY) VALUES(%s,%s,%s,%s,%s)'
val = [
    (901,'NOODELS',100,"VEG","STARTER"),
    (902,'CHOCO LAVA',250,"VEG","SWEET"),
    (903,'FRENCH FIES',100,"VEG","STARTER"),
    (904,'PANEER TIKA',350,"VEG","STARTER"),
    (905,'GARLIC CHESS BREAD',200,"VEG","STARTER"),
    (906,'VEG BIRYANI',240,"VEG","MAIN_COURSE"),
    (907,'DOSA',150,"VEG","MAIN_COURSE"),
    (908,'DOUBLE CHEEZE PIZZA',200,"VEG","STARTER"),
    (909,'FRIED RICE',90,"VEG","MAIN_COURSE"),
    (910,'MANCHURIAN',150,"VEG","STARTER"),
    (911,'MUTTON_CURRY',400,"NON-VEG","MAIN_COURSE"),
    (912,'SAHI PANEER',250,"VEG","MAIN_COURSE"),
    (913,'SAMI KEBAB',300,"NON VEG","STARTER"),
    (914,'BUTTER CHICKER WITH RUMALI ROTI',490,"NON VEG","MAIN_COURSE"),
    (915,'RAJMA CHAWAL',200,"VEG","MAIN_COURSE"),
    (916,'CHICKEN LOLIPOP',350,"NON VEG","STARTER"),
    (917,'SAHI PANEER WITH RICE,CHAPATI,RAYTA',250,"VEG","MAIN_COURSE"),
    (918,'TOMATO SOUP',100,"VEG","STARTER"),
    (919,'MIX VEG WITH 4 CHAPATI',250,"VEG","MAIN_COURSE"),
    (920,'CHICKEN ROAST',550,"NON VEG","MAIN_COURSE"),
    (921,'CHICHEN BURGER',240,"NON VEG","STARTER")
    
]
myacces.executemany(sql,val)
mydb.commit()

#  SELECTING DATA FORM MENU TABLE
myacces.execute('SELECT * FROM MENU')
for rows in myacces:
    print(rows)

# Creating Bill table
myacces.execute('CREATE TABLE BILL (CUST_ID integer NOT NULL,AMOUNT integer NOT NULL,PAID_AMOUNT_INCULDING_TAX integer)')

# DESCRIBING BILL TABLE
myacces.execute('DESC BILL')
for rows in myacces:
    print(rows) 

# INSERTING DATA
sql = 'INSERT INTO BILL(CUST_ID,AMOUNT,PAID_AMOUNT_INCULDING_TAX) VALUES(%s,%s,%s)'
val = [
    (811,250,0),
    (812,150,0),
    (815,1050,0)
]
myacces.executemany(sql,val)
mydb.commit()

# accesing the data
myacces.execute('SELECT * FROM BILL')
for rows in myacces:
    print(rows) 



# DELETING THE  ROW DATA FROM ORDERS TABLE
sql = 'DELETE FROM ORDERS WHERE CUST_ID = 814'
myacces.execute(sql)
mydb.commit()


# fetching the data
myacces.execute('SELECT * FROM ORDERS')
myresult = myacces.fetchall()
for x in myresult:
  print(x)  


# CREATING PREMIUM CUSTOMER AND GIVING  DISSCOUNT
myacces.execute('SELECT * ,CASE WHEN SUB_TOTAL >= 500 THEN "30% OFF" ELSE "10% OFF" END AS "DISCCOUNT" FROM ORDERS')
for i in myacces:
    print(i)

    
# APPLYING TAX ON ORDERS AMOUNT
myacces.execute('SELECT * ,CASE WHEN SUB_TOTAL >= 500 THEN SUB_TOTAL+100 ELSE SUB_TOTAL+50 END FROM ORDERS')
for i in myacces:
    print(i)


# updating paid_amount column from BILL table
sql = 'UPDATE BILL SET PAID_AMOUNT_INCULDING_TAX = CASE WHEN AMOUNT >500 THEN AMOUNT+100 ELSE AMOUNT+50 END '
myacces.execute(sql)
mydb.commit()

# FETCHING DATA
myacces.execute('SELECT * FROM BILL')
for x in myacces:
  print(x)

# Joining Customer ,Order and Bill table
sql = 'SELECT ORDERS.CUST_ID,NAME,ORDERS.ITEM_ID,ORDERS.SUB_TOTAL\
    FROM ORDERS\
    INNER JOIN BILL ON BILL.CUST_ID = ORDERS.CUST_ID\
    INNER JOIN CUSTOMER ON CUSTOMER.CUST_ID = ORDERS.CUST_ID'
    
myacces.execute(sql)

for i in myacces:
    print(i)