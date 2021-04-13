num=list(range(5,51,5))
print(num)
y=0
for x in num:
    print("Index no:", y, "=", x)
    y=y+1
n=int(input("Enter the * No:"))

for i in range(n+1):
    print(n*"*")
    n=n-1