def toh(n, s, a, d):
    if n == 1:
        print('Move disk 1 from rod ', s, ' to ', d)
        return
    toh(n - 1, s, d, a)
    print('Move disk', n, 'from rod ', s, ' to ', d)
    toh(n - 1, a, s, d)


p = int(input("Enter Number of disk: "))
toh(p, 'A', 'B', 'C')
