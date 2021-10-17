a, b, c = map(int, input().split())

i = 1

while True:
    c -= a
    if i % 7 == 0:
        c -= b
    if c <= 0:
        break
    i += 1

print(i)
