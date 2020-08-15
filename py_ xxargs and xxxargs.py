#Xargs: Work like as tuple--
def student(*details):   #Xarg use * (One Star);
    print(details[1])

student(101,"sakib")
student(102,"sajjad",3.3)

def add(num1,num2):
    sum=num1+num2
    print(sum)
add(100,50)

#Using Xarg in addition  function  see below:

def addition(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
addition(100,50)
addition(10,20)
addition(10,20,30)

#Start XXarg : work like as dictonary--

# Using XXarg in student function ,see below:

def student(**details):    #XXagr use ** (Two star) ;
    print(details)
student(id=101,name="imran")
student(id=102,name=  "sajjad")

