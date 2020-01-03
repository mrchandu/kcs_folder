import datetime
import paho.mqtt.client as mqtt
import time
from random import randint
import config
   
while True:
    channel_id = config.channels['channel_id']
    thing_id = config.things['thing_id']
    thing_key = config.things['thing_key']
    
    thing_id1 = config.things['thing_id1']
    thing_key1 = config.things['thing_key1']

    thing_id2 = config.things['thing_id2']
    thing_key2 = config.things['thing_key2']

    para_name="Temperature"
    para_name1="Velocity"
    para_name2="Acceleration"

    value=randint(1,20)
    value1=randint(2,4)
    value2=randint(1,5)
    timestamp=time.ctime()


    d='[{"n":"'+str(para_name)+'","t":'+str(timestamp)+',"v":'+str(value)+'}]'
    d=str(d)
    print(d)
    broker_address= "192.168.1.32"
    port = 1883
    user = thing_id
    password = thing_key
    client = mqtt.Client("Python")
    client.username_pw_set(user, password)
    client.connect(broker_address, port)
    client.loop_start()
    channel_id= channel_id
    client.publish("channels/"+channel_id+"/messages",d)
    time.sleep(3)
    


    """def mqtt_publish(senml_data,thing_id,thing_key,channel_id):
        mqtopic="channels/"+channel_id+"/messages"
        mqtopic=str(mqtopic)

        #print('MQtopic: ',mqtopic)
        #print(senml_data)

        ip="192.168.1.32"
        payload=senml_data
        
        client=mqtt.Client("P1")

        client.username_pw_set(username=thing_id,password=thing_key)
        client.connect(ip,port=1883,keepalive=60,bind_address="")   
        
        client.publish(mqtopic,payload)
        #print('DATA PUBLISHED')
    def mqtt_publish1(senml_data,thing_id1,thing_key1,channel_id):
        mqtopic1="channels/"+channel_id+"/messages"
        mqtopic1=str(mqtopic1)
        #print(senml_data)
        payload1=senml_data
        client=mqtt.Client("P2")
        client.username_pw_set(username=thing_id1,password=thing_key1)
        client.publish(mqtopic1,payload1)
        #print('DATA PUBLISHED')
    def mqtt_publish2(senml_data,thing_id2,thing_key2,channel_id):
        mqtopic2="channels/"+channel_id+"/messages"
        mqtopic2=str(mqtopic2)
        #print(senml_data)
        payload2=senml_data
        #print(payload2)
        client=mqtt.Client("P3")
        client.username_pw_set(username=thing_id2,password=thing_key2)
        client.publish(mqtopic2,payload2)
        print('DATA PUBLISHED')
        time.sleep(2)
    #a = convert_to_senml(para_name,value,sen_ts)
   #b=convert_to_senml1(para_name1,value1,sen_ts)
    c=convert_to_senml2(para_name2,value2,sen_ts)
    # print(c,)
    #mqtt_publish(a,thing_id,thing_key,channel_id)
    #mqtt_publish1(b,thing_id1,thing_key1,channel_id)
    mqtt_publish2(c,thing_id2,thing_key2,channel_id)"""

