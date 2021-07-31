import sys
queue = []
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().rstrip()
    if " " in line:
        command, parameter = line.split()
        if command == 'push':
            queue.insert(0, parameter)
    elif line == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif line == 'size':
        print(len(queue))
    elif line == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif line == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
    elif line == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])


