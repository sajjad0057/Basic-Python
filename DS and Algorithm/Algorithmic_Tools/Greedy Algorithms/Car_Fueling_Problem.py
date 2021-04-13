'''
****There is an issu*****
'''
x = [0,1,4,5,6,8]
l = 3
n = len(x)


def minRefills(x,n,l):
    numRefill = 0
    currentRefill = 0
    while currentRefill<=n:
        print("numRefill ---- : ",numRefill)
        print(x)
        lastRefill = currentRefill
        print("lastRefill ---- > :",lastRefill)
        print(x[currentRefill+1]-x[lastRefill])
        while currentRefill<n-2:
            print("currentRefill --- : ", currentRefill)
            if x[currentRefill+1]-x[lastRefill]<=l:
                currentRefill +=1
            else:
                break

        if currentRefill == lastRefill:
            return "Impossible"
        if currentRefill<=n:
            print("Refill possition : ",x[currentRefill])
            numRefill =+ 1
    return numRefill
y= minRefills(x,n,l)
print(y)

