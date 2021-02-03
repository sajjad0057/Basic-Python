def marge_sort(a,b):
    marged_list = []
    len_a , len_b = len(a),len(b)
    index_a, index_b = 0,0
    #print(f'index_a , index_b = {index_a} , {index_b}')
    while index_a<len_a and index_b<len(b):
        if a[index_a]<b[index_b]:
            marged_list.append(a[index_a])
            index_a +=1
        else:
            marged_list.append(b[index_b])
            index_b +=1
        #print(f'index_a , index_b = {index_a} , {index_b}')
    if index_a<len(a):
        marged_list.extend(a[index_a:])
        #print("****",marged_list)
    if index_b<len(b):
        marged_list.extend(b[index_b:])
        #print("+++++", marged_list)

    return  marged_list





def marge(L):
    if len(L)<=1:
        return L
    mid = len(L)//2
    left = marge(L[:mid])
    right = marge(L[mid:])
    return marge_sort(left,right)




if __name__ == "__main__":
    L = [5, 6, 34, 32, 6, 8, 3, 2, 5, 7, 5, 55, 43, 3, 33, 4, 6, 78]
    sorted_list = marge(L)
    print("Original List : ", L)
    print("Sorted List : ", sorted_list)









