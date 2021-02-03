'''
Better solution:
'''

# def binary_search(l,x):
#     left = 0
#     right = len(l)-1
#     while left<=right:
#         mid = (left+right)//2
#         if l[mid] == x:
#             return f'{x} exist in {mid+1} possition'
#         if l[mid]<x:
#             left = mid+1
#         else:
#             right = mid-1
#     return f'{x} dosen\'t exist'

# l = [1,2,3,4,5,6,7,78,88,99]
# print(binary_search(l,999))

'''
naive solution :
'''
def recursivly_binary_search(arr, low, high, x):

    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return f'{x} exist in {mid+1} possition'
        elif arr[mid] > x:
            return recursivly_binary_search(arr, low, mid - 1, x)
        else:
            return recursivly_binary_search(arr, mid + 1, high, x)
    else:
        return f'{x} dosen\'t exist'


# Test array
arr= [1,2,3,4,5,6,7,78,88,99]
x = 99

# Function call
result = recursivly_binary_search(arr, 0, len(arr) - 1,x )

print(result)
