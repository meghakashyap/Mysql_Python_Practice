
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Megha@8287',
    database = 'demo'
)

mycursor = mydb.cursor()

# Creating Table
# mycursor.execute('CREATE TABLE BUDGET (TENTANT VARCHAR(50),YEAR integer,SALES integer)')

# Adding rows
# sql = "INSERT INTO BUDGET (TENTANT,YEAR,SALES) VALUES(%s,%s,%s)"
# val = [
#     ('tentant1',2014,2000),
#     ('tentant2',2012,5000),
#     ('tentant3',2013,1000),
#     ('tentant4',2014,1500),
#     ('tentant5',2015,800)
# ]

# mycursor.executemany(sql,val)
# mydb.commit()

# selcting data
# mycursor.execute("SELECT * FROM BUDGET ")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
  
  
# Adding new column in existing table
# mycursor.execute('ALTER TABLE BUDGET ADD  YOY varchar(30) not null')


# Describing table
# mycursor.execute('DESC BUDGET')
# for x in mycursor:
#   print(x)


# storing sales column in list
mycursor.execute("SELECT SALES FROM BUDGET ")
result = mycursor.fetchall()
sales = []
for y in result:
    for y_ in y:
        sales.append(y_)



# storing year column in list  
mycursor.execute("SELECT YEAR FROM BUDGET ")
result = mycursor.fetchall()
years = []
for x in result:
    for x_ in x:
        years.append(x_)

# print(sales)
# print(years)


# Finding YOY
values = []
i = 0
while i<len(years):
    print(years[i],"hy")
    if years[i]>years[i-1]:
        print(years[i])
        yoy = ((sales[i]-sales[i-1])/sales[i-1])*100
        values.append(yoy)
    else:
        values.append(" ")
    i+=1
        
print(values)


# Inserting values in new column
sql = "UPDATE BUDGET SET YOY = -46.6666666666666 WHERE  TENTANT = 'tentant5'"
mycursor.execute(sql)
mydb.commit()
    
print(mycursor.rowcount, "record(s) affected")

