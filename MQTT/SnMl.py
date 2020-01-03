import paho.mqtt.client as mqtt
import time
from random import randint
import datetime

#Temperature = randint(1,20)
Velocity = randint(1,6)
Acceleration = randint(1,3)

ts=time.time()
timestamp=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
timestamp=str(timestamp)
#d = '[{ "n":"'+str(para_name)+'","t":'+str(timestamp)+',"v":'+str(Temperature)+'}]'
#d = '[{ "n":"'+str(para_name)+'","v":'+str(value)+'}]'

broker_address= "192.168.1.32"
port = 1883
user = "818d02d4-3b9f-4890-87dc-38a91c173f9d"
password = "b11cd727-034c-4fe6-98c2-d51f71a5d337"
client = mqtt.Client("Python")
client.username_pw_set(user, password)
client.connect(broker_address, port)
client.loop_start()
"""channel_id="aee0cd8c-1332-4399-be26-db39d2faa62c"
thing_id="818d02d4-3b9f-4890-87dc-38a91c173f9d"
thing_key="b11cd727-034c-4fe6-98c2-d51f71a5d337"""

channel_id="34a44798-40fa-44fb-9323-a516b03dee19"
thing_id="ce3fba1b-b85f-470e-8e4a-d9011e721060"
thing_key="0b81cb64-5f40-4932-9f91-4e9c2a4e7dc1"
#lsof -i -P -n | grep 8086
"""{
  "id": "ce3fba1b-b85f-470e-8e4a-d9011e721060",
  "key": "0b81cb64-5f40-4932-9f91-4e9c2a4e7dc1",
  "name": "tata"
}"""


while True:
    para_name = "Temperature"
    Temperature = randint(1,20)
    d = '[{ "n":"'+str(para_name)+'","t":'+str(timestamp)+',"v":'+str(Temperature)+'}]'
    dstr=str(d)
    print(d)
    client.publish("channels/"+channel_id+"/messages",dstr)
    time.sleep(2)