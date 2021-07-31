from math import gcd

def lcm(_a, _b):
    return _a * _b // gcd(_a, _b)

t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    print(lcm(a, b))


