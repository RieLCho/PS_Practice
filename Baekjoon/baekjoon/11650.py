n = int(input())
inputList = []
for i in range(n):
    inputList.append(list(map(int, input().split())))
inputList.sort(key=lambda r: (r[0], r[1]))
for i in inputList:
    print(i[0], i[1])
