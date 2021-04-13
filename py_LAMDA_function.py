'''
*lambda function has no name.
* lambda function is called "Anonymous function",
* Not powerfull as named function.
* lambda function work with single Expression/Single line Code.
** lambda function Syntax:
    "(lambda parameter : expression)(argument)"
'''
#At first named function given below:
def cal(a,b): #This is called named function.cz we use function name.
    return a+b
sum=cal(10,5)
print("The sum is:",sum)

#lambda function given below:
rule=(lambda a,b: a*a+2*a*b+b*b)(2,3)
print(rule)

#Or:

print((lambda a,b:a+b)(2,3))

