# Fibonacci_Number naive algorithm :

'''
using Recursion :
More Expensive solution : avoid this
'''
# n = int(input("Enter a Number : "))
#
# def FibRecurs(n):
#     if n<=1:
#         return n
#     else:
#         return FibRecurs(n-1)+FibRecurs(n-2)
# x = FibRecurs(n)
# print(x)


'''
Fibonacci_Number fast algorithm :
BEST SOLUTION
'''

# nth_terms = int(input("Enter a number : "))
# n1, n2=0, 1
# i = 0
#
# if nth_terms <=0 :
#     print("Please Enter positive number : ")
# elif nth_terms == 1:
#     print(n1)
# else:
#     while i<nth_terms:
#         nth = n1+n2
#         print(f'{n1}')
#         n1 = n2
#         n2 = nth
#         i +=1
#     print(i)



'''
Another:
BETTER SOLUTION :
'''
nth_terms = int(input("Enter a number : "))
list = [0,1]
if nth_terms <=0 :
    print("Please Enter positive number : ")
elif nth_terms == 1:
    print(list[0])

else:
    for i in range(2,nth_terms):
        list.append(list[i-1]+list[i-2])
        print(list)
    print(list[i])



