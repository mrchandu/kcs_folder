import datetime
import paho.mqtt.client as mqtt
import time
import json
broker_url = "192.168.1.9"
broker_port = 1883
client = mqtt.Client()
def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code "+(rc))
def on_message(client, userdata, message):
    #print("Message received: "  + str(message.payload.decode("utf-8")))
    json_data = str(message.payload.decode("utf-8"))
    json_parsed = json.loads(json_data)
    json_object = json_parsed['object']
    Temperature = json_object['Distance']
    global value 
    value = Temperature
    print(value)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)
client.subscribe("application/1/device/30a59a8db698bb16/rx")
client.loop_start()
value = ''
while True:
    thing_id="24cb063a-c1aa-4b7e-a3e7-eae290462bfa"
    thing_key="0c06e321-25f2-4bff-ab60-9080e32388ff"
    channel_id="e5a6c256-7075-4ad0-b4e1-df67f1343b58"

    para_name="Distance"
    
    ts=time.time()
    timestamp=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    timestamp=str(timestamp)

    
    date_time_str=timestamp
    date_time_obj=datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
               
    sen_ts=time.mktime(date_time_obj.timetuple())
    sen_ts=int(sen_ts)
    def convert_to_senml(para_name,value,timestamp):
        d = '[{ "n":"'+str(para_name)+'","ut":'+str(timestamp)+',"t":'+str(timestamp)+',"v":'+str(value)+'}]'
        d=str(d)
        return d
    def mqtt_publish(senml_data,thing_id,thing_key,channel_id):
        mqtopic="channels/"+channel_id+"/messages"
        mqtopic=str(mqtopic)

        ip="35.154.33.195"
        payload=senml_data
        #print(payload)
        client=mqtt.Client("P1")

        client.username_pw_set(username=thing_id,password=thing_key)
        client.connect(ip,port=1883,keepalive=60,bind_address="")   
        
        client.publish(mqtopic,payload)
        #print("published....")
    
    a = convert_to_senml(para_name,value,sen_ts)
    mqtt_publish(a,thing_id,thing_key,channel_id)