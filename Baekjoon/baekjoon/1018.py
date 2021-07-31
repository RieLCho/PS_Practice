n, m = map(int, input().split())
board = []
count = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        case1Counter = 0
        case2Counter = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] == 'B':
                        case1Counter += 1
                    if board[k][l] == 'W':
                        case2Counter += 1
                else:
                    if board[k][l] == 'W':
                        case1Counter += 1
                    if board[k][l] == 'B':
                        case2Counter += 1
        count.append(min(case1Counter, case2Counter))
print(min(count))

