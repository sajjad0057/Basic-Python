l = [1,4,2,65,32,654,22,334]

def insertion_sort(l):
    for i in range(1,len(l)):
        item = l[i]
        j = i-1
        while j>=0 and l[j]>item:
            l[j+1]=l[j]
            j -=1
            print(l)
        l[j+1] = item
    return l

print(l)
print("Finaly insertion sorted array : ",insertion_sort(l))