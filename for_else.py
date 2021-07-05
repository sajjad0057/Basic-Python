'''
for loops also have an else clause which most of us are unfamiliar with.
The else clause executes after the loop completes normally.
This means that the loop did not encounter a break statement.
'''


# for i in range(1, 11):
#     if i%2==0:
#         print(f'{i} is even number')
#
# else:
#     print("No break")


for n in range(2, 10):
    print("n--- : ",n)
    for x in range(2, n):
        print(f'{n} no of x : {x}')
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


