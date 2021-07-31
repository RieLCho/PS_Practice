n, m, L = map(int, input().split())

d = [[int(x) for x in input().split()] for y in range(n)]
p = [[int(x) for x in input().split()] for y in range(L)]

diff = [[0 for x in range(L - 1)] for y in range(m)]
for i in range(L - 1):
    for j in range(m):
        diff[i][j] = p[i + 1][j] - p[i][j]

for i in range(L - 1):
    for j in range(n):
        if diff[i] == d[j]:
            print(j + 1)
            break
