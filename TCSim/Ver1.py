import time

max =50
start = time.time()
def tempfun():
    global temp
    temp = 1
    while temp < 50:
        #time.sleep(1)
        temp +=1
        remaining = max + start - time.time()
        print("Temperature :",temp)
        if remaining <= 0:
            break
start1 = time.time()
def Accelfun():
    global Acce
    Acce = 0
    while Acce <2:
        #time.sleep(1)
        Acce +=1
        remaining = max + start - time.time() 
        print("Acceleration :",Acce)
        if remaining <=0:
            break
start2 = time.time()
def Velofun():
    global velo
    velo = 0
    while velo < 4:
        velo +=1
        #time.sleep(1)
        remaining = max + start - time.time()
        print("Velocity :",velo)
        if remaining <=0:
            break


while True:
    tempfun()
    Accelfun()
    Velofun()
    time.sleep(2)