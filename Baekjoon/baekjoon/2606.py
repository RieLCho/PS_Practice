computerCount = int(input())
connected = int(input())
arr = [[0] * computerCount for i in range(computerCount)]
visit = [0 for i in range(computerCount)]
for i in range(connected):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    arr[b - 1][a - 1] = 1

def dfs(v):
    visit[v] = 1
    for i in range(computerCount):
        if arr[v][i] == 1 and visit[i] == 0:
            dfs(i)

dfs(0)
result = 0
for i in range(1, computerCount):
    if visit[i] == 1:
        result += 1
print(result)