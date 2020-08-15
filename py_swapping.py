a=int(input("Enter the No. of a:"));
b=int(input("Enter the No. of b:"));

'''
temp = a;
a = b;
b = temp;      [this is conventional  swapping system]
print("before swapping a=",a);
print("before swapping b=",b);
'''
# python swapping system given below:

a,b=b,a;
print("before swapping a=",a);
print("before swapping b=",b);