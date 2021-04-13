def partition(L,low,high):
    pivot = L[high]
    i = low - 1
    for j in range(low,high):
        if L[j]<pivot:
            i +=1
            L[i],L[j] = L[j],L[i]
            print(L)
    L[i+1],L[high] = L[high],L[i+1]
    return i+1


def quick_sort(L,low,high):
    if low>=high:
        return
    p = partition(L,low,high)
    quick_sort(L,low,p-1)
    quick_sort(L,p+1,high)


L = [1,5,6,3,8,6,4,7,2,6]
print("Old list    -----> : ",L)
quick_sort(L,0,len(L)-1)
print("Sorted list -----> : ",L)