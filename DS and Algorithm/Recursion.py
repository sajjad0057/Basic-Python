def f(n):
    if n<=1:
        return n
    print(n-1,n-2)
    return f(n-1)+f(n-2)
print(f(7))