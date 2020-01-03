import mysql.connector
from mysql.connector import Error
import time

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="etag@123",
  database="OMRON"
)

mycursor = mydb.cursor()

temp =345
Accel = 12
Veloc = 23
load = 1


sql = "INSERT INTO prusight_plc(Temperature_value, Velocity_value, Acceleration_value,Motor_load) VALUES (%s, %s, %s,%s)"
val = (temp,Accel,Veloc,load)

mycursor.execute(sql, val)

mydb.commit()