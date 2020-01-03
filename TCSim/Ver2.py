"""import time

max = 31
start = time.time()
while True:
    ### Do other stuff, it won't be blocked
    time.sleep(0.1)
    print("looping...")

    ### This will be updated every loop
    remaining = max + start - time.time()
    print("%s seconds remaining" % int(remaining))

    ### Countdown finished, ending loop
    if remaining <= 0:
        break"""
import time
limit = 0
while limit < 30 :
    time_a = time.time()
    """ Your code here """
    [print("1111111111111111111",i) for i in list(range(1,50,1))]
    [print("2222222222222222222",j) for j in list(range(1,10,1))]
    time_spent = time.time() - time_a
    if time_spent < 2:
        time.sleep(1 - time_spent)
    print("%s seconds remaining" % (limit))
    limit = limit -1