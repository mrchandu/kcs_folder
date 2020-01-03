import datetime
import paho.mqtt.client as mqtt
import time
import json
from random import randint
while True:
    thing_id="b6095dd5-0a82-4b26-9abf-88333e212db2"#24cb063a-c1aa-4b7e-a3e7-eae290462bfa"
    thing_key="51a3e3a8-5a36-4e51-9017-1e305d1c53b7"#0c06e321-25f2-4bff-ab60-9080e32388ff"
    channel_id="3dee7c4a-1b09-4165-9c16-53db1d00518b"#e5a6c256-7075-4ad0-b4e1-df67f1343b58"

    para_name="vinay"
    
    ts=time.time()
    timestamp=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    timestamp=str(timestamp)
    date_time_str=timestamp
    date_time_obj=datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    sen_ts=time.mktime(date_time_obj.timetuple())
    sen_ts=int(sen_ts)
    print(sen_ts)
    value = randint(1,30)
    def convert_to_senml(para_name,value,timestamp):
        d = '[{ "n":"'+str(para_name)+'","ut":'+str(timestamp)+',"t":'+str(timestamp)+',"v":'+str(value)+'}]'
        d=str(d)
        return d
    def mqtt_publish(senml_data,thing_id,thing_key,channel_id):
        mqtopic="channels/"+channel_id+"/messages"
        mqtopic=str(mqtopic)

        ip="192.168.1.32"
        payload=senml_data
        client=mqtt.Client("P1")

        client.username_pw_set(username=thing_id,password=thing_key)
        client.connect(ip,port=1883,keepalive=60,bind_address="")   
        
        client.publish(mqtopic,payload)
        print("published....")
    
    a = convert_to_senml(para_name,value,sen_ts)
    mqtt_publish(a,thing_id,thing_key,channel_id)