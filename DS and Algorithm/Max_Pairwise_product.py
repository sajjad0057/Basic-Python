# n = int(input("Enter The no of array length : "))
# num = []
# for i in range(n):
#     x = int(input())
#     num.append(x)
# result = 0
# for i in num:
#     for j in num:
#         if i != j:
#             x = i*j
#             if x>=result:
#                 result = x
#
# print("Maximum Pairwise product :",result)

# def max_pairwise_product_naive(a):
#     result = 0
#     for i in a:
#         for j in a:
#             if i != j:
#                 x = i*j
#                 if x>=result:
#                     result = x
#     return result





'''
Best solution below :

'''
def max_pairwise_product_naive(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            result = max(result,a[i]*a[j])

    return result



def max_pairwise_product_fast(a):
    index_1 = 0
    for i in range(1,len(a)):
        if a[i]>a[index_1]:
            index_1 = i
    index_2 = 0
    for j in range(1,len(a)):
        if a[index_1] != a[j] and a[j]>a[index_2]:
            index_2 = j
    return a[index_1]*a[index_2]


n = int(input("Enter The no of array length : "))
num = []
for i in range(n):
    x = int(input())
    num.append(x)
print("max_pairwise_product_first ---->",max_pairwise_product_fast(num))
print("max_pairwise_product_naive ---->",max_pairwise_product_naive(num))
