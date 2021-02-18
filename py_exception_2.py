x = int(input("Enter greater than ten : "))
try:
    if x < 10:
        raise ValueError("Number less then ten")
except ValueError as f:
    print(f)

