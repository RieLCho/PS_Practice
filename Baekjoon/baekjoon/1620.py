from sys import stdin

n, m = map(int, stdin.readline().split())

dogam = []
dogam_index = {}
for i in range(n):
    a = stdin.readline().rstrip()
    dogam.append(a)
    dogam_index[a] = i + 1
for i in range(m):
    temp = stdin.readline().rstrip()
    if temp.isnumeric():
        print(dogam[int(temp)-1])
    else:
        print(dogam_index[temp])