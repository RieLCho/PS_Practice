from math import ceil
n, k = map(float, input().split())
n = int(n)
s = 0
for i in range(n):
    s += float(input())

print(ceil(s/k))