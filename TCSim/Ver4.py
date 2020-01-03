from multiprocessing import Process
import time

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Etag@1234",
    database = "sensor"
)
mycursor = mydb.cursor()
"""Temperature = 0
Acceleration = 0
Velocity = 0

sql = "INSERT INTO data(Temperature,Acceleration,Vibration) VALUES ('%s','%s',%s)" % (Temperature,Acceleration,Velocity)
mycursor.execute(sql)"""
def loop_a():
    while True:
        Temperature =0
        while Temperature <= 20:
            Temperature +=1
            mycursor = mydb.cursor()
            sql = "INSERT INTO data(Temperature) VALUES ('%s')" % (Temperature)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            now1 = time.time()
            print("A",Temperature,now1)
    time.sleep(1)
def loop_b():
    while True:
        Acceleration = 0
        while Acceleration <=1:
            Acceleration +=1
            mycursor = mydb.cursor()
            sql = "INSERT INTO data(Acceleration) VALUES ('%s')" % (Acceleration)
            mycursor.execute(sql)
            mydb.commit()
            now1 = time.time()
            print("Acceleration",Acceleration,now1)
    time.sleep(1) 
#out_Accel = 1
def loop_c():
    while True:
        Velocity = 3
        while Velocity <=4:
            Velocity +=1
            mycursor = mydb.cursor()
            sql = "INSERT INTO data(Vibration) VALUES ('%s')" % (Velocity)
            mycursor.execute(sql)
            mydb.commit()
            now = time.time()
            print("Velocity",Velocity,now)
    #time.sleep()
if __name__ == '__main__':

    Process(target=loop_a).start()
    Process(target=loop_b).start()
    Process(target=loop_c).start()