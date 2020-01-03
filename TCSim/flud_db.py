import time
import mysql.connector
from random import randint
mydb = mysql.connector.connect(
    host = "192.168.1.32",
    user = "root",
    passwd = "etag@1234",
    database = "mainflux_table"
)
mycursor = mydb.cursor()
Temperature = randint(10,20)
Acceleration = randint(1,5)
Vibration = randint(20,40)
time_now = time.strftime('%Y-%m-%d %H:%M:%S') 
loadvalue = randint(15,25)
voltage_v1 = randint(230,240)
voltage_v2 = randint(15,25)
voltage_v3 = randint(15,25)
current_c1 = randint(15,25)
current_c2 = randint(15,25)
current_c3 = randint(15,25)
powerfactor = randint(15,25)
activepower = randint(15,25)
reactivepower = randint(15,25)
total_power = randint(15,25)
frequency = randint(50,60)
while True:
    sql = "INSERT INTO mainflux_table(TEMP_K6CM, VELOCITY_K6CM, ACCELRATION_K6CM, timestamp_value, load_value, INSTANTANEOUS_VOLTAGE_V1, INSTANTANEOUS_VOLTAGE_V2, INSTANTANEOUS_VOLTAGE_V3, INSTANTANEOUS_CURRENT_C1, INSTANTANEOUS_CURRENT_C2, INSTANTANEOUS_CURRENT_C3, INSTANTANEOUS_POWERFACTOR, INSTANTANEOUS_FREQUENCY, INSTANTANEOUS_ACTIVEPOWER, INSTANTANEOUS_REACTIVEPOWER, TOTAL_POWER) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (Temperature,Acceleration,Vibration,time_now, loadvalue, voltage_v1, voltage_v2, voltage_v3, current_c1, current_c2, current_c3, powerfactor, frequency, activepower, reactivepower, total_power)
    mycursor.execute(sql)
    mydb.commit()

