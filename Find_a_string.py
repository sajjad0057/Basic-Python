string, substring = (input().strip(), input().strip())
sum = 0
for i in range(len(string)-len(substring)+1):
    print(f'{1+i} -------> {[ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]}')
    if string[i:i+len(substring)] == substring:
        sum +=1
print(sum)
# print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))