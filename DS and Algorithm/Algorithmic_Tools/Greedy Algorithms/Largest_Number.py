# num = input("Enter the number : ")
# list = []
# for i in num:
#     list.append(i)
# list.sort(reverse=True)
# y = ''
# for x in list:
#     y +=x
# print("The Bigest Number is : ",y)

num = int(input("Enter the Number of digit : "))
number = []
for i in range(num):
    number.append(int(input(f'Enter the digit no - {i+1} : ')))
number.sort(reverse=True)
print("The Largest number is : ",end='')
for i in number:
    print(i,end="")





