n = int(input())
xCoordinate = [0 for _ in range(n+1)]
yCoordinate = [0 for _ in range(n+1)]
xCount = [0 for _ in range(100001)]
yCount = [0 for _ in range(100001)]

for i in range(1, n+1, 1):
    x, y = map(int, input().split())
    xCoordinate[i] = x
    yCoordinate[i] = y
    xCount[x] += 1
    yCount[y] += 1

result = 0
for i in range(1, n+1, 1):
    if yCount[yCoordinate[i]] > 1 and xCount[xCoordinate[i]] > 1:
        result += (yCount[yCoordinate[i]]-1) * (xCount[xCoordinate[i]]-1)

print(result)