import multiprocessing
import time

def cal_sqr(n,r):
    for idx , i in enumerate(n):
        time.sleep(0.5)
        r[idx] = i*i

if __name__ == "__main__":
    n = [1,2,3,4,5]
    r = multiprocessing.Array('i',5)
    p = multiprocessing.Process(target=cal_sqr,args=(n,r))

    p.start()
    p.join()

    print(f'RESULT : {r[:]}')