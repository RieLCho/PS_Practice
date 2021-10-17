n, t, c, p = map(int, input().split())
a = n//t
if n%t == 0:
    a -= 1
print(int(a*c*p))