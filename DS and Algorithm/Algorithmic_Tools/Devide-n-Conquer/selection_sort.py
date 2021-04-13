l = [4,3,2,2,1]
def selection_sort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index=j
        if min_index != i:
            l[i],l[min_index]=l[min_index],l[i]
            print(l)

    return l

print("Finaly sorted array : ",selection_sort(l))