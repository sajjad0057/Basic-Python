num={1,2,5,4,7,7,7,6,5}
print("1---->",num)   #set r not print same or duplicate value.
print("2--->",9 in num )
print("3---->",4 in num )
num2=[1,2,2,2,3,4,5] #it was list
print("4---->",num2)

num3=set(num2) #num2 list converted to set
print("5----->",num3)
num4=num3|num
num5=num3&num
num6=num3-num
print("6----->",num4)
print("7----->",num5)
print("8----->",num6)
num.add(9)
print("9---->",num)
num.remove(2)
print("10---->",num)
