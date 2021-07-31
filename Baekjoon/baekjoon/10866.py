import sys
deque = []
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().rstrip()
    if " " in line:
        command, parameter = line.split()
        if command == 'push_front':
            deque.insert(0, parameter)
        elif command == 'push_back':
            deque.append(parameter)
    elif line == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif line == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif line == 'size':
        print(len(deque))
    elif line == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif line == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif line == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])


