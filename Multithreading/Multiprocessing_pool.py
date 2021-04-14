import multiprocessing
import time

def func(n):
    sum = 0
    for x in range(10000):
        sum += x
    return sum






if __name__ == "__main__":

    p = multiprocessing.Pool()
    t1 = time.time()
    r = p.map(func,range(10000))    # map(function, iterables)

    p.close()
    p.join()

    print("Pool took time :",time.time() - t1)

    t2 = time.time()

    arr = list()

    for x in range(10000):
        arr.append(func(x))

    print("Serial processing took : ",time.time() - t2)
