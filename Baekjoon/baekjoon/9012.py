t = int(input())
for i in range(t):
    l = list(input())
    checksum = 0
    for i in l:
        if i is '(':
            checksum += 1
        elif i is ')':
            checksum -= 1
        if checksum < 0:
            print('NO')
            break
    if checksum > 0:
        print('NO')
    elif checksum is 0:
        print('YES')