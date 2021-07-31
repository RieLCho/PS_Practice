from sys import stdin, stdout

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
compareList = list(map(int, stdin.readline().split()))
l.sort()
for cursor in compareList:
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == cursor:
            result = 1
            break
        elif l[mid] > cursor:
            end = mid - 1
        else:
            start = mid + 1
    print(result)