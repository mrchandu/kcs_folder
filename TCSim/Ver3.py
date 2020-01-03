from multiprocessing import Process
import time

    
def loop_a():
    while True:
        Temperature =0
        while Temperature <= 20:
            Temperature +=1
            print("A",Temperature)
            time.sleep(2)
 
def loop_b():
    while True:
        Acceleration = 0
        while Acceleration <=1:
            Acceleration +=1
            print("Acceleration",Acceleration)
            time.sleep(2)

def loop_c():
    while True:
        Velocity = 3
        while Velocity <=4:
            Velocity +=1
            print("Velocity",Velocity)
            time.sleep(2)

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
    Process(target=loop_c).start()
    
    