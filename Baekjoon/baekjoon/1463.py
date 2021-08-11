n = int(input())
l = [0 for _ in range(n+1)]
for i in range(2, n+1):
    l[i] = l[i-1] + 1
    if i%2 == 0 and l[i] > l[i//2] + 1:
        l[i] = l[i//2] + 1
    if i%3 == 0 and l[i] > l[i//3] + 1:
        l[i] = l[i//3] + 1

print(l[n])