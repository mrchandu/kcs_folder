import json
from random import randint
import time
import datetime
import mysql.connector
mydb = mysql.connector.connect(
    host = "192.168.1.59",
    user = "root",
    port = "3307",
    passwd = "mypassword",
    database = "Etag"
)
mycursor = mydb.cursor()
while True:
    now = datetime.datetime.now().replace(microsecond=0)
    print(now)
    Sensor1 = str(randint(20,40))
    Sensor2 = str(randint(10,400))
    Sensor3 = str(randint(0,60))
    res = Sensor1+'|'+Sensor2+'|'+Sensor2+'\n'

    with open("mysql_data.txt", 'w') as result:
        result.write(res)
    with open("mysql_data.txt", 'r') as result:
        x=result.readlines()
    full=len(x)
    for i in range(full):
        
        x1 = x[i].split('|')
        sen1 = str(x1[0])
        sen2 = str(x1[1])
        sen3 = str(x1[2])
        now.strftime('%Y-%m-%d %H:%M:%S')
        print(sen1,sen2,sen3)
        sql = "INSERT INTO Tata_Coffee (Sensor1, Sensor2,Sensor3, Time) VALUES (%s, %s,%s,%s)"
        val = (sen1,sen2,sen3,now)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        time.sleep(3)