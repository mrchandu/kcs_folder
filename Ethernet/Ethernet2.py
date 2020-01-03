import logging
import sys
import time
import threading
import cpppo
from cpppo.server.enip import poll
from cpppo.server.enip.get_attribute import proxy_simple as device
import paho.mqtt.client as mqttClient
hostname='192.168.1.49'
params  = [('@0xf5/1/1','INT')]#,('@1/1/7','SSTRING')]
def failure( exc ):
    failure.string.append( str(exc) )
failure.string          = [] # [ <exc>, ... ]

def process( par, val ):
    #process.values[par]        = val
    process.values[par] = val
process.done            = False

process.values          = {} # { <parameter>: <value>, ... }
poller              = threading.Thread(
    target=poll.poll, kwargs={
        'proxy_class':  device,
        'address':  (hostname, 44818),
        'cycle':    1.0,
        'timeout':  0.5,
        'process':  process,
        'failure':  failure,
        'params':   params,
    })
poller.start()
try:
    while True:
        while process.values:
            par,val=process.values.popitem()
            data = val[0]
            broker_address= "192.168.1.105"
            port = 1883
            user = "818d02d4-3b9f-4890-87dc-38a91c173f9d"
            password = "b11cd727-034c-4fe6-98c2-d51f71a5d337"
            client = mqttClient.Client("Python")
            client.username_pw_set(user, password=password)
            #client.on_connect= on_connect
            client.connect(broker_address, port=port)
            client.loop_start()
            channel_id="aee0cd8c-1332-4399-be26-db39d2faa62c"
            thing_id="818d02d4-3b9f-4890-87dc-38a91c173f9d"
            thing_key="b11cd727-034c-4fe6-98c2-d51f71a5d337"
            client.publish("channels/"+channel_id+"/messages",data)
        while failure.string:
            exc = failure.string.pop( 0 )
            print("%s: %s" %(time.ctime(), exc))
        time.sleep(1)
finally:
    process.done = True
    poller.join()
#channel_id="aee0cd8c-1332-4399-be26-db39d2faa62c"
#thing_id="818d02d4-3b9f-4890-87dc-38a91c173f9d"
#thing_key="b11cd727-034c-4fe6-98c2-d51f71a5d337"
