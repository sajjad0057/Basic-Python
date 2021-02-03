'''
For integers, a and b, their greatest common divisor or gcd(a,b) is the largest integer d so that
d divides both a and b.
'''

'''
naive solution :
'''
# x = int(input("Enter The 1st number : "))
# y = int(input("Enter The 2nd Number : "))
# z = min(x,y)
# gcd = 0
# for i in range(1,z):
#     if x%i == 0 and y%i == 0:
#         gcd = i
# print(gcd)


#Another :
'''
Better Solution :

'''
num1 = int(input("Enter The 1st number : "))
num2 = int(input("Enter The 2nd Number : "))

while(num2 != 0):
# swap using temp variable
  temp = num2
  num2 = num1 % num2
  num1 = temp
gcd = num1
print(gcd)