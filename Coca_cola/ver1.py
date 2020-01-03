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
#sql = "SELECT TEMP_K6CM  FROM `prusight_dv_vibration_sensor_1` WHERE id='1'"
#TEMP_K6CM`, `VELOCITY_K6CM`, `ACCELRATION_K6CM`,`load_value`, `INSTANTANEOUS_VOLTAGE_V1`, `INSTANTANEOUS_VOLTAGE_V2`, `INSTANTANEOUS_VOLTAGE_V3`, `INSTANTANEOUS_CURRENT_C1`, `INSTANTANEOUS_CURRENT_C2`, `INSTANTANEOUS_CURRENT_C3`, `INSTANTANEOUS_POWERFACTOR`, TOTAL_POWER` 
sql = "SELECT `TEMP_K6CM`, `VELOCITY_K6CM`, `ACCELRATION_K6CM` FROM `prusight_dv_vibration_sensor_1` WHERE id='700'"
mycursor.execute(sql)

myresult = mycursor.fetchall()
print(myresult)
for x in myresult:
  print(x)
