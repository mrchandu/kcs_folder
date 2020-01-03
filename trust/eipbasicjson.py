import logging
import sys
import time
import threading
import cpppo
from cpppo.server.enip import poll
from cpppo.server.enip.get_attribute import proxy_simple as device
import json
global ip, tag, dtype
ip = str()
tag = str()
dtype = str()

with open('/root/Desktop/eip/prusight_ethernetip/eipcred.txt') as json_file:
    data = json.load(json_file)
    for v in data.values():
        
        ip = v["enipip"]
        tag = v["eniptag"]
        dtype = v["enipdtype"]
       

'''EIPdata=list()
MYSQLdata=list()
FLUXdata=list()'''

#initialise Ethernet/IP
'''def EIP_intialise():
    
    eipurl=input("Enter Ethernet/IP host url : ")
    eiptag=input("Enter Ethernet/IP tag (@class/instance/attribute) : ")
    eipdtype=input("Enter Ethernet/IP tag datatype : ")
    EIPdata.append(eipurl)
    EIPdata.append(eiptag)
    EIPdata.append(eipdtype)'''

#initialise MYSQL
"""def mysql_initialise():
    sqlhost=input("Enter SQL host address : ")
    sqluser=input("Enter SQL host username : ")
    sqlpwd=input("Enter SQL host password : ")
    dbname=input("Enter SQL database name : ")
    MYSQLdata.append(sqlhost)
    MYSQLdata.append(sqluser)
    MYSQLdata.append(sqlpwd)
    MYSQLdata.append(dbname)

    try:
        mydb =mysql.connector.connect(host=sqlhost,user=sqluser,passwd=sqlpwd,database=dbname)
        mycursor=mydb.cursor()
        print("Connected to MySQL Server Database")
        #GUI.sql_pop1()
        #configdict.update({"SQL Host":sqlhost})
        #configdict.update({"SQL Username":sqluser})
        #configdict.update({"SQL Password":sqlpwd})
        #configdict.update({"Database Name":dbname})

        #DB.get_db(mydb)
        #MYSQL_list.append(mydb)
    
    except:
        try:
            mydb=mysql.connector.connect(host=sqlhost,user=sqluser,passwd=sqlpwd)
            mycursor=mydb.cursor()
            db="CREATE DATABASE "+dbname
            db=str(db)
            mycursor.execute(db)
            
            mydb=mysql.connector.connect(host=sqlhost,user=sqluser,passwd=sqlpwd,database=dbname)
            mycursor=mydb.cursor()
            mycursor.execute("CREATE TABLE EDATA1(ATTRIBUTEID VARCHAR(255),THINGID VARCHAR(255),THINGKEY VARCHAR(255),CHANNELID VARCHAR(255))")
            mycursor.execute("CREATE TABLE EDATA2(TAG VARCHAR(255), VAL VARCHAR(255),TIME_STAMP VARCHAR(255))")
            print("New database and table(EDATA) created. Connected to MySQL Server Database")
            #GUI.sql_pop2()

            #configdict.update({"SQL Host":sqlhost})
            #configdict.update({"SQL Username":sqluser})
            #configdict.update({"SQL Password":sqlpwd})
            #configdict.update({"Database Name":dbname})

            #DB.get_db(mydb)
            #MYSQL_list.append(mydb)
        
        except:
            print("'Error - could not connect to MySQL Server")
            #GUI.sql_error()


def mainflux_initialise():
        
    flux_ip=input("Enter mainflux ip address : ")
    flux_port=input("Enter mainflux port : ")
    flux_email=input("Enter mainflux user id : ")
    flux_pwd=input("Enter mainflux user password : ")
    
    FLUXdata.append(flux_ip)
    FLUXdata.append(flux_port)
    FLUXdata.append(flux_email)
    FLUXdata.append(flux_pwd)

    try:
        token=MF.get_token(flux_ip,flux_port,flux_email,flux_pwd)
        print("Connected to Mainflux")
        #GUI.flux_pop()
        #configdict.update({"Mainflux IP":flux_ip})
        #configdict.update({"Mainflux Port":flux_port})
        #configdict.update({"Mainflux Email":flux_email})
        #configdict.update({"Mainflux Password":flux_pwd})
    except:
        print("Error - could not connect to Mainflux")
        #GUI.flux_error()"""

#routine to start ENIP,MYSQL and Mainflux functions
"""EIP_intialise()
mysql_initialise()
mainflux_initialise()

#routine to create new thing and channel and for adding thing to channel

channelname=input("Enter new channel name : ")

MF.new_channel(channelname)
MF.new_thingid(channelname)
chid=MF.fluxlist[3]
chid=str(chid)
thid=MF.fluxlist[4]
thid=str(thid)
MF.new_thingkey(thid)
MF.add_thing_to_channel(chid,thid)
thkey=MF.fluxlist[5]
thkey=str(thkey)

ts=time.ctime()"""

#main Ethernet/IP routine
hosturl=ip
ENIPTAG=tag
ENIPDTYPE=dtype
#hosturl="192.168.1.103"
#ENIPTAG="@1/1/2"
#ENIPDTYPE="INT"

hostname=hosturl
params=[(ENIPTAG,ENIPDTYPE)]

def failure(exc):
    failure.string.append(str(exc))
failure.string=[] # [ <exc>, ... ]

def process( par, val ):
    process.values[par] = val
process.done = False

process.values	= {} # { <parameter>: <value>, ... }

poller = threading.Thread(
    target=poll.poll, kwargs={
        'proxy_class':  device,
        'address': 	(hostname, 44818),
        'cycle':	1.0,
        'timeout':	0.5,
        'process':	process,
        'failure':	failure,
        'params':	params
    })
poller.start()

try:
    while True:
        while process.values:
            par,val=process.values.popitem() 
            TAG1 = par[0]
            VALUE1 = val[0]
	    print("value :",VALUE1)
            #print(TAG1,"-",VALUE1)
            #EIPdata.append(TAG1)
            #EIPdata.append(VALUE1)
            #routine to insert data into MYSQL DB
            """mydb=mysql.connector.connect(host=MYSQLdata[0],user=MYSQLdata[1],passwd=MYSQLdata[2],database=MYSQLdata[3])
            mycursor=mydb.cursor()
            sql1="INSERT INTO EDATA1(ATTRIBUTEID,THINGID,THINGKEY,CHANNELID) VALUES (%s,%s,%s,%s)"
            val1=(TAG1,thid,thkey,chid)
            sql2="INSERT INTO EDATA2(TAG,VAL,TIME_STAMP) VALUES (%s,%s,%s)"
            val2=(TAG1,VALUE1,ts)

            mycursor.execute(sql1, val1)
            mycursor.execute(sql2, val2)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

                #senml payload conversion
            d = '[{ "n":"'+str(TAG1)+'","t":'+str(ts)+',"v":'+str(VALUE1)+'}]'
            d=str(d)
            print(d)

            #routine for MQTT PUSH
            broker_address=FLUXdata[0]
            port = 1883
            user = thid
            password = thkey
            client = mqtt.Client("Python")
            client.username_pw_set(user, password)
            client.connect(broker_address, port)
            client.loop_start()
            channel_id=chid
            client.publish("channels/"+channel_id+"/messages",d)
            print("Pushing via MQTT started")"""

                
        while failure.string:
            exc	= failure.string.pop( 0 )
            print("%s: %s" %(time.ctime(), exc))
        time.sleep(2)
finally:
    process.done = True
    poller.join()

