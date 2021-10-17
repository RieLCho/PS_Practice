input = list(map(int, input().split()))
target = [1, 1, 2, 2, 2, 8]
for i in range(len(input)):
    print(target[i] - input[i], end=' ')