import json
import time
import mysql.connector
mydb = mysql.connector.connect(
    host = "103.44.220.9",
    user = "prusight_dev",
    passwd = "I3cGivPqdpI1",
    database = "prusight_dev"
)
mycursor = mydb.cursor()
x1 = [(1,2,0.01), (1,2,0.01), (1,2,0.01),(1,2,0.01), (1,2,0.01), (1,2,0.01)]
x2 = [(2,3.0,0.02),(3,3.1,0.03), (4,3.2,0.04), (5,3.3,0.05),(6,3.4,0.06),(7,3.5,0.07),(8,3.6,0.08),(9,3.7,0.09),(10,3.8,0.10),(11,3.9,0.11),(12,4.0,0.12),(13,4.1,0.13),(14,4.2,0.14),(15,4.3,0.15),(16,4.4,0.16),(17,4.5,0.17),(18,4.6,0.18),(19,4.7,0.19),(20,4.8,0.20),(21,4.9,0.21),(22,5.0,0.21),(23,5.1,0.22),(24,5.2,0.23),(25,5.3,0.24),(26,5.4,0.25),(27,5.5,0.26),(28,5.6,0.27),(29,5.7,0.28),(30,5.8,0.29),(31,5.9,0.30),(32,6.0,0.31),(33,6.1,0.32),(34,6.2,0.33),(35,6.3,0.34),(36,6.4,0.35),(37,6.5,0.36),(38,6.6,0.37),(39,6.7,0.39),(40,6.8,0.4),(41,6.9,0.5),(42,7.0,0.6),(43,7.1,0.7),(44,7.2,0.8),(45,7.3,0.86),(46,7.5,0.89),(47,7.6,0.9),(48,7.8,0.92),(49,7.9,0.95),(50,8,1.00)]


def fun1():

    a = 0
    while a <2:
        for Temperature,Vibration,Acceleration in x1:
            print(Temperature,Vibration,Acceleration)
            time_now = time.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO prusight_dv_vibration_sensor_2(temperature_value, velocity_value, acceleration_value, timestamp_value) VALUES ('%s','%s','%s','%s')" % (Temperature,Acceleration,Vibration,time_now)
            mycursor.execute(sql)
            mydb.commit()
            time.sleep(5)
        a +=1
        if a == 2:
            break

    b = 0
    while b < 3:
        for Temperature,Vibration,Acceleration in x2:
            print(Temperature,Vibration,Acceleration)
            time_now = time.strftime('%Y-%m-%d %H:%M:%S') 
            sql = "INSERT INTO prusight_dv_vibration_sensor_2(temperature_value, velocity_value, acceleration_value, timestamp_value) VALUES ('%s','%s','%s','%s')" % (Temperature,Acceleration,Vibration,time_now)
            mycursor.execute(sql)
            mydb.commit()
            time.sleep(5)
        b +=1
        if b == 3:
            break
while True:
    a = 0
    while a <4:
        fun1()

        a =+1
        if a ==4:
            break