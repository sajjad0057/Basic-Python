'''
Multithreading Vs Multiprocessing :

Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other.
This gives you the illusion that the threads are running in parallel,but they are actually run in a concurrent manner.
In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.


Multiprocessing is a technique where parallelism in its truest form is achieved.
Multiple processes are run across multiple CPU cores, which do not share the resources among them.
Each process can have many threads running in its own memory space.
In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.
'''

import time
import multiprocessing

sqr_res = []
def cal_sqr(arr):
    for i in arr:
        time.sleep(0.5)
        print(f'SQR : {i*i}')
        sqr_res.append(i*i)
    print("SQR RESULT : ", sqr_res)


# cube_res = []
# def cal_cube(arr):
#     for i in arr:
#       time.sleep(0.5)
#       print(f'CUBE : {i*i*i}')

if __name__ == "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target=cal_sqr,args=(arr,))
    # p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("SQR RESULT out side: ", sqr_res)
    print("Done")