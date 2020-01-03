import paho.mqtt.client as mqttClient
from random import randint
def on_message(client, userdata, message):
    print("Message received: "  + str(msg.payload.decode("utf-8")))
while True:
    broker_address= "35.154.33.195"
    port = 1883
    client = mqttClient.Client("mosquitto")    #client.on_connect= on_connect
    client.connect(broker_address, port=port)
    client.connect = on_message
    client.subscribe("#")
    