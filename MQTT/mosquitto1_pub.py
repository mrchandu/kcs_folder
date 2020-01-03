import paho.mqtt.client as mqttClient
from random import randint
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload.decode("utf-8")))

mqttc = mqttClient.Client()
mqttc.on_message = on_message
broker_address= "192.168.1.59"
port = 1883
mqttc.connect(broker_address,port)
print("Mosquitto running.......!")

while True:
    data = randint(1,20)
    data1 = randint(20,50)
    data2 = randint(1,5)
    data3 = randint(2,17)
    mqttc.publish("Temperature",data)
    mqttc.publish("Velocity",data1)
    mqttc.publish("Acceleration",data2)
    mqttc.publish("Load",data3)
