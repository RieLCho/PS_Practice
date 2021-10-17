from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

arr = []
count = 0


def postOrderPrint(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            division = i
            break

    postOrderPrint(start + 1, division - 1)
    postOrderPrint(division, end)
    print(arr[start])


while count <= 10000:
    try:
        n = int(input())
    except:
        break
    arr.append(n)
    count += 1

postOrderPrint(0, len(arr) - 1)
