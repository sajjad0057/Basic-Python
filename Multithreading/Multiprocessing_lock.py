'''
python multiprocess Lock and shared memory
Multiprocess Lock

lock = multiprocessing.Lock() creates a lock
lock.acquire() acquisition lock
lock.release() release lock
with lock: Automatic acquisition and release locks are similar to with open() as f:
Characteristic:

Who grabs the lock first and who executes it first.
After the execution of the process is completed, other processes grab the lock and execute it again.
'''


import time
import multiprocessing

def deposite(blns,lock):
    for i in range(50):
        time.sleep(0.01)
        lock.acquire()
        blns.value = blns.value + 1
        lock.release()

def withdraw(blns,lock):
    for i in range(50):
        time.sleep(0.01)
        lock.acquire()
        blns.value = blns.value - 1
        lock.release()

if __name__ == "__main__" :
    blns = multiprocessing.Value('i',300)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposite,args=(blns,lock))
    w = multiprocessing.Process(target=withdraw,args=(blns,lock))

    d.start()
    w.start()
    d.join()
    w.join()

    print(f'{blns.value}')