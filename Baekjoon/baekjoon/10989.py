import sys
n = int(sys.stdin.readline())
MAX_SIZE = 10001
arr = [0]*MAX_SIZE
for i in range(n):
    arr[int(sys.stdin.readline())] += 1
for i in range(MAX_SIZE):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
