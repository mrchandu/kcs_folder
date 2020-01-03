import datetime
import paho.mqtt.client as mqtt
import requests
import time
from random import randint
import config

while True:
    channel_id = "da155866-b292-43cd-9ec4-8535678315d1"#config.channels['channel_id']
    thing_id2 = config.things['thing_id2']
    thing_key2 = config.things['thing_key2']
    para_name2="Acceleration"
    value2=randint(1,5)
    ts=time.time()
    timestamp=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    timestamp=str(timestamp)

    
    date_time_str=timestamp
    date_time_obj=datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
               
    sen_ts=time.mktime(date_time_obj.timetuple())
    sen_ts=int(sen_ts)
    def convert_to_senml2(para_name2,value2,timestamp):
        d2 = '[{ "n":"'+str(para_name2)+'","ut":'+str(timestamp)+',"t":'+str(timestamp)+',"v":'+str(value2)+'}]'
        d2=str(d2)
        return d2
    def mqtt_publish2(senml_data,thing_id2,thing_key2,channel_id):
        mqtopic2="channels/"+channel_id+"/messages"
        mqtopic2=str(mqtopic2)
        payload2=senml_data
        client=mqtt.Client("P")
        client.username_pw_set(username=thing_id2,password=thing_key2)
        client.publish(mqtopic2,payload2)
        print('DATA PUBLISHED')
        time.sleep(2)
    c = convert_to_senml2(para_name2,value2,timestamp)
    mqtt_publish2(c,thing_id2,thing_key2,channel_id)