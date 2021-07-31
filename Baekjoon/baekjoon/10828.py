import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().rstrip()
    if " " in line:
        command, parameter = line.split()
        if command == 'push':
            stack.insert(0, parameter)
    elif line == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif line == 'size':
        print(len(stack))
    elif line == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif line == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])



