# def compareTriplets(a, b):
#     x = 0
#     y = 0
#     for i in range(len(a)):
#         if a[i]>b[i]:
#             x +=1
#         elif a[i]==b[i]:
#             continue
#         else:
#             y +=1
#     return f'{x} {y}'

'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

Syntax
zip(iterator1, iterator2, iterator3 ...)
'''

def compareTriplets(a, b):
    x , y = 0 , 0
    for m,n in zip(a,b):
        if m>n:
            x +=1
        elif m<n:
            y +=1
    return f'{x} {y}'


'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
Syntax
map(function, iterables)
'''


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)