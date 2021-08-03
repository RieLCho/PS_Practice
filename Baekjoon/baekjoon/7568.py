n = int(input())
inputList = []
for i in range(n):
    inputList.append(list(map(int, input().split())))

for i in inputList:
    count = 1
    for j in inputList:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count, end=' ')