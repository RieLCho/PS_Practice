n, b = map(str, input().split())
b = int(b)
temp = 1
result = 0
for i in range(len(n) - 1, -1, -1):
    if '0' <= n[i] <= '9':
        a = ord(n[i]) - ord('0')
    else:
        a = ord(n[i]) - ord('A') + 10

    a *= temp
    result += a
    temp *= b

print(result)