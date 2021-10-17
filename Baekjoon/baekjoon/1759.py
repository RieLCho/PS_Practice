from itertools import combinations

l, c = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
candidate = sorted(list(map(str, input().split())))

comb = combinations(candidate, l)

for cursor in comb:
    cnt = 0
    for letter in cursor:
        if letter in vowels:
            cnt += 1
    if 1 <= cnt <= l-2:
        print(''.join(cursor))
