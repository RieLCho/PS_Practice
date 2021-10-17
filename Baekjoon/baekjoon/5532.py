from math import ceil
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

etaLiterature = int(ceil(a/c))
etaMath = int(ceil(b/d))

print(l - max(etaMath, etaLiterature))

