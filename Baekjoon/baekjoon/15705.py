# 세로 확인
def doesRowHaveSubstring():
    for i in range(n):
        for j in range(m):
            a = int(i)
            b = int(j)
            temp = ''
            while a < n and b < m:
                temp += (chart[a][b])
                a += 1
            if (s in temp) or (s[::-1] in temp):
                return True
            temp = ''
    return False


# 가로 확인
def doesColHaveSubstring():
    for i in range(n):
        for j in range(m):
            a = int(i)
            b = int(j)
            temp = ''
            while a < n and b < m:
                temp += (chart[a][b])
                b += 1
            if (s in temp) or (s[::-1] in temp):
                return True
            temp = ''
    return False


# 우대각선 확인
def doesRightDiagonalHaveSubstring():
    for i in range(n):
        for j in range(m):
            a = int(i)
            b = int(j)
            temp = ''
            while a < n and b < m:
                temp += (chart[a][b])
                a += 1
                b += 1
            if (s in temp) or (s[::-1] in temp):
                return True
            temp = ''
    return False


# 좌대각선 확인
def doesLeftDiagonalHaveSubstring():
    for i in range(n):
        for j in range(m):
            a = int(i)
            b = int(j)
            temp = ''
            while a > -1 and b > -1:
                try:
                    temp += (chart[a][b])
                except IndexError:
                    pass
                a += 1
                b -= 1
            if (s in temp) or (s[::-1] in temp):
                return True
            temp = ''
    return False


s = input()
n, m = map(int, input().split())
chart = [list(input()) for _ in range(m)]

if doesRightDiagonalHaveSubstring():
    print(1)
elif doesLeftDiagonalHaveSubstring():
    print(1)
elif doesRowHaveSubstring():
    print(1)
elif doesColHaveSubstring():
    print(1)
else:
    print(0)
