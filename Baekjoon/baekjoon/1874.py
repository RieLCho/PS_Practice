n = int(input())
answer = []
stack = []
cnt = 1
for i in range(n):
    inputNum = int(input())
    while cnt <= inputNum:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == inputNum:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit()
for i in answer:
    print(i)