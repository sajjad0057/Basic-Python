number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(revs_number))





# def reverse(x):
#     y = str(x)
#     if y[0] == "-":
#         r = y[:0:-1]
#         print(f'-{r}')
#     else:
#         print(y[::-1])
#
# reverse(-0)


# x = -134335
# y = str(x)
# print(y,type(y))