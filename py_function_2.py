import math as m
x=m.factorial(9)
print(x)

def hello():
    print("Hello world")
    print(input("how are you"))
hello()

#global variable:
outer=10
def display_value():
    inner=5
    print(f"outer={outer} and inner is={inner}")
display_value()
print(inner) #error occured.

help(print)



'''
here factorial(),print(),input are library function.
And hello() is user define function
'''

