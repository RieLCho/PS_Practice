n = int(input())
l = [0 for _ in range(2*n)]
min = 200001
l = list(map(int, input().split()))
l.sort()

for i in range(0, 2*n):
    temp = l[i] + l[len(l)-1-i]
    if temp < min:
        min = temp

print(min)

