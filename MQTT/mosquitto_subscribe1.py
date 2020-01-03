import paho.mqtt.client as mqtt
import time
import mysql.connector
mydb = mysql.connector.connect(
    host = "103.44.220.9",
    user = "prusight_dev",
    passwd = "I3cGivPqdpI1",
    database = "prusight_dev"
)
mycursor = mydb.cursor()

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code " (rc))

def on_message_from_Temperature(client, userdata, message):
   print("Message Recieved from Temperature: "+message.payload.decode())
   global Temperature
   Temperature = message.payload.decode()

def on_message_from_Velocity(client, userdata, message):
   print("Message Recieved from Velocity: "+message.payload.decode())
   global Velocity
   Velocity = message.payload.decode()

def on_message_from_Acceleration(client, userdata, message):
   print("Message Recieved from Acceleration: "+message.payload.decode())
   global Acceleration
   Acceleration = message.payload.decode()
   
def on_message_from_Load(client, userdata, message):
   print("Message Received from Load: "+message.payload.decode())
   Load = message.payload.decode()
   time_now = time.strftime('%Y-%m-%d %H:%M:%S')
   sql = "INSERT INTO prusight_dv_vibration_sensor_1(temperature_value,velocity_value,acceleration_value,timestamp_value,load_value) VALUES ('%s','%s','%s','%s','%s')" % (Temperature,Velocity,Acceleration,time_now,Load)
   mycursor.execute(sql)
   mydb.commit()
   print("Data Inserted")
   time.sleep(2)

def on_message(client, userdata, message):
   #print("Message Recieved from Others: "+message.payload.decode())
   pass

broker_url = "192.168.1.59"
broker_port = 1883
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("Temperature",qos=1)
client.subscribe("Velocity",qos=1)
client.subscribe("Acceleration", qos=1)
client.subscribe("Load",qos=1)
client.message_callback_add("Temperature", on_message_from_Temperature)
client.message_callback_add("Velocity", on_message_from_Velocity)
client.message_callback_add("Acceleration", on_message_from_Acceleration)
client.message_callback_add("Load", on_message_from_Load)

client.loop_forever()