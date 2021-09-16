import threading
import time
import random

def execute_thread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    
    rand_sleep_time = random.randint(1, 4)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Active Threads:", threading.activeCount())
    print("Thread Objects:", threading.enumerate())