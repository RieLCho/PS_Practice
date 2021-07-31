from sys import stdin, stdout

def isPrimeNumber(_n):
    if _n <= 1:
        return False
    elif _n is 2:
        return True
    for i in range(2, _n):
        if _n % i is 0:
            return False
    return True

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
counter = 0
for cursor in l:
    if isPrimeNumber(cursor):
        counter += 1
print(counter)
