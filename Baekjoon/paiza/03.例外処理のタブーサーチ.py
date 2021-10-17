n, m, L = map(int, input().split())

d = [[int(x) for x in input().split()] for y in range(n)]
p = [[int(x) for x in input().split()] for y in range(L)]

diff = [[0 for x in range(L - 1)] for y in range(m)]
for i in range(L):
    for j in range(m):
        try:
            diff[i][j] = p[i + 1][j] - p[i][j]
        except IndexError:
            pass

isValid = False

for i in range(n):
    for j in range(n):
        for k in range(m):
            if diff[i][k] != d[j][k]:
                isValid = False
                break
        if isValid:
            print(j+1)