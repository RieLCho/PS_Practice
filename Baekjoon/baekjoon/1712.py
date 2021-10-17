a, b, c = map(int, input().split())
if b == c:
    print(-1)
    exit()
m = -(a/(b-c))
if m < 0:
    print(-1)
    exit()
if m is not int:
    m = int(m) + 1
print(m)