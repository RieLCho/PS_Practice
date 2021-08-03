n = int(input())
inputList = []
for i in range(n):
    inputList.append(list(map(int, input().split())))
inputList.sort(key=lambda l: (l[1], l[0]))
for cursor in inputList:
    print(cursor[0], cursor[1])