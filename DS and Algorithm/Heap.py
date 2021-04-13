# heap_size=int(input('input heap size: '))
# i=1
# heap = [None] * heap_size
# while i:
#     print('i------->',i)
#     if i==heap_size//2:
#         break
#
#
#
#     if i==1:
#         root = input('please input root first: ')
#         heap[i]=root
#     if i<heap_size:
#         left=input(f'please input left child in {heap[i]}: ')
#         heap[i*2]=left
#         right=input(f'please input right child in {heap[i]}: ')
#         heap[i * 2 + 1] = right
#         i+=1



def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2


# def is_max_heap(H):
#     n=len(H)-1
#     for i in range(n,1,-1):
#         p=parent(i)
#         if H[p]<H[i]:
#             return False
#     return True

def max_heapify(heap, heap_size ,i):
    l=left(i)
    r=right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest=l
    else:
        largest=i

    if r <= heap_size and heap[r] > heap[largest]:
        largest=r

    if largest != i:
        heap[i],heap[largest]=heap[largest],heap[i]
        max_heapify(heap,heap_size,largest)

def build_max_heap(heap):
    heap_size=len(heap)-1
    for i in range(heap_size//2,0,-1):
        max_heapify(heap,heap_size,i)


heap=[None,55,66,72,62,67,71,77,63,99]

print(heap)
max_heapify(heap,len(heap)-1,1)
print(heap)
# H=[None,19,7,17,3,5,12,10,1,4]
# print(H,is_max_heap(H))
# H=[None,1,2,3]
# print(H,is_max_heap(H))
# H=[None,2,1,3]
# print(H,is_max_heap(H))
# H=[None,3,1,2]
# print(H,is_max_heap(H))