for a in range(int(input())):
    if a != 0:
        print()
    n = int(input())
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    print(n, end='')
    if s == n:
        print(" is a perfect number.")
    elif s < n:
        print(" is a deficient number.")
    else:
        print(" is an abundant number.")