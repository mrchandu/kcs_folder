import mysql.connector
mydb = mysql.connector.connect(
    host = "192.168.1.59",
    user = "root",
    port = "3307",
    passwd = "mypassword",
    database = "Etag"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM Tata_Coffee" #WHERE Sensor1 ='1'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)