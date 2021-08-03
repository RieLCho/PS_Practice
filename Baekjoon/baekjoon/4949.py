from sys import stdin
while True:
    s = list(str(stdin.readline()[:-1]))
    if s == ['.']:
        break

    stack = []
    for cursor in s:
        if cursor == '(' or cursor == '[':
            stack.append(cursor)
        elif cursor == ')':
            if len(stack) == 0:
                print('no')
                break
            if stack.pop() != '(':
                print('no')
                break
        elif cursor == ']':
            if len(stack) == 0:
                print('no')
                break
            if stack.pop() != '[':
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')