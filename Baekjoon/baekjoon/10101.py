a = list(int(input()) for _ in range(3))

if sum(a) == 180:
    if a[0] == a[1] == a[2]:
        print("Equilateral")
    elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")