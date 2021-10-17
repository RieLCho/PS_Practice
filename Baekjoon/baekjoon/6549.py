while True:
    test = list(map(int, input().split()))
    if test[0] == 0 and len(test) == 1:
        break
    test.append(0)
    result = 0
    stack = [[0, 0]]
    for cursor in range(1, test[0] + 2):
        while stack[-1][1] > test[cursor]:
            temp = stack.pop()
            temp_area = 0
            while stack[-1][1] == temp[1]:
                stack.pop()
            temp_area = max((cursor - 1 - stack[-1][0]) * temp[1], (cursor - temp[0]) * temp[1])
            result = max(temp_area, result)
        stack.append([cursor, test[cursor]])
    print(result)