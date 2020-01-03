import schedule
import time
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Etag@1234',
    database = 'sensor'
)

curser = mydb.cursor()
Temperature=2
Acceleration=3
Velocity=4
a = 1
while a < 10 :
    sql = "INSERT INTO data(Temperature,Acceleration,Vibration) VALUES ('%s','%s','%s')" % (Temperature,Acceleration,Velocity)
    curser.execute(sql)
    mydb.commit()
    time.sleep(2)
    a +=1
    if a == 9:
        break

def job():
    Temperature = 0
    Velocity = 0
    Acceleration = 0
    while Temperature < 18 and Velocity < 5 and Acceleration <1:
        Temperature +=1
        Velocity +=1
        Acceleration +=1
        sql = "INSERT INTO data(Temperature,Acceleration,Vibration) VALUES ('%s','%s','%s')" % (Temperature,Acceleration,Velocity)
        curser.execute(sql)
        mydb.commit()
        print(Temperature,Acceleration,Velocity)
        time.sleep(2)

schedule.every(0.1).minutes.do(job)










"""
import time
limit = 0
while limit < 30:
    time_a = time.time()
    print(1)
    time_spent = time.time() - time_a
    if time_spent < 0.5:
        time.sleep(1 - time_spent)
    print("%s seconds remaining" % (limit))
    limit = limit -1

Temp = 0
Vibra = 0
Accel = 0
while Temp < 180 and Vibra < 180 and Accel < 180:
    Temp +=1
    Vibra +=1
    Accel +=1
    print(Temp,Vibra,Accel)

"""
