import time

def cal_sqr(n):
    print("Calculated Square Number : ")
    for i in n:
        time.sleep(0.5)
        print('SQR : ', i*i)


def cal_cube(n):
    print("Calculated Cube of Numbers : ")
    for i in n:
        time.sleep(0.5)
        print("CUBE : ",i*i*i)

arr = [1,2,3,4,5]

t = time.time()
cal_sqr(arr)
cal_cube(arr)

print("Done In : ",time.time() - t)
print("Yah ! .... I am done my all work now .")