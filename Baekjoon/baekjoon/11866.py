n, k = map(int, input().split())

queue = []
result = []
cursor = -1
for i in range(n):
    queue.append(i + 1)

while queue:
    for _ in range(k):
        cursor += 1
        if cursor > len(queue) - 1:
            cursor = 0
    result.append(queue[cursor])
    queue.pop(cursor)
    cursor -= 1

print("<", end='')
for i in range(n):
    if i == n - 1:
        print(str(result[i])+'>')
    else:
        print(str(result[i]) + ", ", end='')
