n = int(input())
result = 0
if n is 0:
    print(0)
else:
    for i in range(2, n + 1, 1):
        if i % 5 is 0:
            result += 1
        if i % 25 is 0:
            result += 1
        if i % 125 is 0:
            result += 1
    print(result)
