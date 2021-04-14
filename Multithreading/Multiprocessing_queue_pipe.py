import multiprocessing
import time

def cal_sqr(n,queue):
    for idx , i in enumerate(n):
        # time.sleep(0.5)
        queue.put(i*i)

if __name__ == "__main__":
    n = [1,2,3,4,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_sqr,args=(n,q))

    p.start()
    p.join()

    while q.empty() is not True:
        print(f'RESULT : {q.get()}')