import random

def max_pairwise_product_naive(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            result = max(result,a[i]*a[j])

    return result



def max_pairwise_product_fast(a):
    index_1 = -1
    for i in range(len(a)):
        if index_1 ==-1 or a[i]>a[index_1]:
            index_1 = i
    index_2 = -1
    for j in range(len(a)):
        if index_1 != j and (index_2 == -1 or a[j]>a[index_2]):   
            index_2 = j
    return a[index_1]*a[index_2]

def test_stress(N,M):
    while True:
        n = random.randint(2,N)
        print("n --->",n)
        a = [random.randint(0,M) for i in range(n)]
        print("a---->",a)

        x=max_pairwise_product_naive(a)
        y=max_pairwise_product_fast(a)
        if x == y:
            print("okk")
        else:
            print("Wrong",x,y)
            break

N = 5
M = 9
test_stress(N,M)
