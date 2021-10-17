from math import sqrt


def isPrimeNumber(x):
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


n = int(input())
result = 0
for i in range(n, 1000001):
    if i == 1:
        continue
    else:
        if str(i) == str(i)[::-1]:
            if isPrimeNumber(i):
                result = i
                break
if result == 0:
    result = 1003001
print(result)
