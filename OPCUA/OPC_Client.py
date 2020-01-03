from opcua import Client
import time
#import mysql.connector

"""mydb = mysql.connector.connect(
    host = 'Localhost',
    user = 'root',
    passwd = 'Abcd@1234#',
    database = 'OPC_SENSOR_DATA'
)"""

url = "opc.tcp://192.168.1.59:40315"
#url = "opc.tcp://192.168.1.59:41891"
client = Client(url)
"""client.set_security_string(
		"Basic256Sha256,"
		"SignAndEncrypt,"
		"my_cert.der,"
		"my_private_key.pem")"""
client.connect()
print("Client Connected....!")
"""while True:
    #mycurser = mydb.cursor()
    Temp = client.get_node("ns=2;i=3")
    Temperature = Temp.get_value()
    
    Accel = client.get_node("ns=2;i=4")
    Acceleration = Accel.get_value()
    
    
    #Time = client.get_node("ns=2;i=5")
    #TIME = Time.get_value()
    
    
    Velo = client.get_node("ns=2;i=5")
    Velocity = Velo.get_value()
    

    Humi = client.get_node("ns=2;i=6")
    Humidity = Humi.get_value()
    
    
    Mois = client.get_node("ns=2;i=7")
    Moisture = Mois.get_value()
    
    
    
    print("Data inserting...")
    print("Temperature" + '-' + str(Temperature),'  '"Acceleration" + '-' + str(Acceleration),'   '"Velocity" + '-' + str(Velocity),'  '"Humidity" + '-' + str(Humidity),'  '"Moisture" + '-' + str(Moisture))
    time.sleep(5)"""