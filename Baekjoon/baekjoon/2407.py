from math import factorial

n, m = map(int, input().split())
denominator = factorial(n-m)*factorial(m)
numerator = factorial(n)

print(numerator//denominator)
