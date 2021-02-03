#l = [7,6,3,4,2]
l = [22,3,55,3,7,11]


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                print(l)
    return l
print("finaly bubble sorted array : ",bubble_sort(l))