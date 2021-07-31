n = int(input())
inputList = []
for i in range(n):
    inputInt, inputString = map(str, input().split())
    inputInt = int(inputInt)
    inputList.append((inputInt, inputString))

inputList.sort(key=lambda r: (r[0]))

for cursor in inputList:
    print(cursor[0], cursor[1])
