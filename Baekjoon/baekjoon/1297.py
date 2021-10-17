from math import sqrt
d, h, w = map(int, input().split())
x = sqrt(d**2/(h**2+w**2))

print(int(x*h), int(x*w))
