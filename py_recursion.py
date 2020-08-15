'''
*Recursion is a process where a function can call itself
*To stop this calling we need a base case
** Two important points in case of recursion is:
   -Recursive call.
   -Base call.
'''
#finding Factorial value of a number:

def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the No:"))
result=factorial(n)
print(result)