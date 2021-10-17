n = int(input())
l = list(input())
temp = len(l)
for i in range(n-1):
    a = list(input())
    for j in range(temp):
        if l[j] != a[j]:
            l[j] = '?'

print("".join(l))