import logging
import sys
import time
import threading

import cpppo
#cpppo.log_cfg['level'] = logging.DETAIL
#logging.basicConfig( **cpppo.log_cfg )

from cpppo.server.enip import poll
from cpppo.server.enip.get_attribute import proxy_simple as device # MicroLogix
#from cpppo.server.enip.get_attribute import proxy as device # ControlLogix
#from cpppo.server.enip.ab import powerflex_750_series as device # PowerFlex 750

# Device IP in 1st arg, or 'localhost' (run: python -m cpppo.server.enip.poll_test)
#from GUITEST import IP_address

hostname='192.168.1.103'

# Parameters valid for device; for *Logix, others, try:
#params = [('@0xf5/1/2','INT')]
params  = [('@0xf5/1/1','INT'),('@1/1/7','SSTRING')]
#params = [ "Motor Velocity", "Output Current" ]

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

# Monitor the process.values {} and failure.string [] 
try:
    while True:
        while process.values:
            #par,val        = process.values.popitem()
            par,val=process.values.popitem()
            #print("%r" % val)
            #par,val=process.values.popitem()
            #print(val[0], val[1])
            #print(val[0])
            #Temp=val[0]
            print(val)

            # print("%s: %16s == %r" % (time.ctime(), par, val))
        while failure.string:
            exc         = failure.string.pop( 0 )
            print("%s: %s" %(time.ctime(), exc))
        time.sleep(1)
finally:
    process.done        = True
    poller.join()