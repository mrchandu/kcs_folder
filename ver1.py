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
    Temperature = json_object['AVI1_Voltage']
    #Digital3     = float(Temperature)/2.5*2
    #print("Temp",Temperature)
    #global value 
    value = Temperature
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)
client.subscribe("application/3/device/11a78101004140a8/rx")
#client.subscribe("application/1/device/30a59a8db698bb16/rx")
client.loop_start()
value=24
while True:
    thing_id="4487712c-7e8e-48ea-9484-90db5558e59c"
    thing_key="469a3242-4d15-4b70-88e5-598f4a1869d2"#aa1baf49-4c71-4b55-8e12-e61c6a279f21"
    #thing_key="2c878dcd-1124-47c8-b2cd-7e8f96d03b65"
    channel_id="7aabb36b-9fdd-498b-b9d3-bc1cdec5cd80"#~829f120b-83a5-4b2c-b753-5ac8088c93b1"

    para_name="Temperature"
    
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
        print("published....")
    
    a = convert_to_senml(para_name,value,sen_ts)
    mqtt_publish(a,thing_id,thing_key,channel_id)
    time.sleep(5)