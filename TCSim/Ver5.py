from multiprocessing import Process
import time

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Etag@1234",
    database = "sensor"
)
mycursor = mydb.cursor()

def loop_a():
    while True:
        Acceleration = 0.1
        while Acceleration <=2:
            Acceleration +=0.1
            print(Acceleration)
            sql = "INSERT INTO data(Acceleration) VALUES ('%s')" % (Acceleration)
            mycursor.execute(sql)
            mydb.commit()
            time.sleep(5)
def loop_b():
    while True:
        Vibration = 0
        while Vibration <=5:
            Vibration +=1
            sql = "INSERT INTO data(Vibration) VALUES ('%s')" % (Vibration)
            mycursor.execute(sql)
            mydb.commit()
            time.sleep(5)

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()