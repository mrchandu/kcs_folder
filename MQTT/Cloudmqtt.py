import paho.mqtt.client as mqttClient
import time
import mysql.connector
from random import randint
mydb = mysql.connector.connect(
    host = "103.44.220.9",
    user = "prusight_dev",
    passwd = "I3cGivPqdpI1",
    database = "prusight_dev"
)
mycursor = mydb.cursor()
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                
        Connected = True                 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print("Message received: "  + str(message.payload))
 
Connected = False
 
broker_address= "m14.cloudmqtt.com"   #Broker address
port = 19786                          #Broker port
user = "pserzwxn"                    #Connection username
password = "JwgICBTk7hdL"            #Connection password
 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
#client.subscribe("python/test")

 
try:
    while True:
        #test = randint(10,20)
        #client.publish("python/test",test)
        #client.subscribe("python/test")
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()