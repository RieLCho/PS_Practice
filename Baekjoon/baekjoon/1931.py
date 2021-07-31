n = int(input())
result = []

for i in range(n):
    start, end = map(int, input().split())
    result.append([start, end])

result = sorted(result, key=lambda a: a[0])
result = sorted(result, key=lambda a: a[1])

endTime = 0
counter = 0
for i, j in result:
    if i >= endTime:
        counter += 1
        endTime = j

print(counter)
