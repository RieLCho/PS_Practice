h, w = map(int, input().split())
arr = list(map(int, input().split()))
result = [0 for _ in range(w)]
for i in range(w):
    mLeft = max(arr[:i+1])
    mRight = max(arr[i:])
    result[i] = abs(arr[i] - min(mLeft, mRight))

print(sum(result))