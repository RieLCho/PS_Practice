n = int(input())
result = abs(100 - n)
m = int(input())
if m:
    button = set(input().split())
else:
    button = set()

for num in range(1000001):
    for cursor in str(num):
        if cursor in button:
            break
    else:
        result = min(result, (abs(num - n) + len(str(num))))

print(result)

