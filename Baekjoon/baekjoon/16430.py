a, b=map(int, input().split())
p = b - a
q = b
if q % p == 0:
    q = q//p
    p = p//p
print(p, q)
