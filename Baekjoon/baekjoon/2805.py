n, m = map(int, input().split())
listHeightInput = list(map(int, input().split()))
left = 1
right = max(listHeightInput)

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for cursor in listHeightInput:
        if cursor >= mid:
            sum += cursor - mid

    if sum >= m:
        left = mid + 1
    else:
        right = mid -1
print(right)
