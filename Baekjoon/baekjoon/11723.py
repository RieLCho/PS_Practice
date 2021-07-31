import sys

s = set()
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().rstrip()
    if " " in line:
        command, parameter = line.split()
        parameter = int(parameter)

        if command == 'add':
            if parameter in s:
                continue
            else:
                s.add(parameter)

        elif command == 'remove':
            if parameter not in s:
                continue
            else:
                s.remove(parameter)

        elif command == 'check':
            if parameter in s:
                print(1)
            else:
                print(0)

        elif command == 'toggle':
            if parameter in s:
                s.remove(parameter)
            else:
                s.add(parameter)

    elif line == 'all':
        s = set([i for i in range(1, 21)])

    elif line == 'empty':
        s.clear()
