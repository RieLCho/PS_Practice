n = int(input())
if n ** 0.5 % 1 == 0:
    print(1)
    exit()

flag = False

for i in range(1, int((n // 2) ** 0.5) + 1):
    for j in range(1, int((n - i ** 2) ** 0.5) + 1):
        if i ** 2 + j ** 2 == n:
            print(2)
            exit()
        elif (n - (i ** 2 + j ** 2)) ** 0.5 % 1 == 0:
            flag = True

if flag:
    print(3)
else:
    print(4)
