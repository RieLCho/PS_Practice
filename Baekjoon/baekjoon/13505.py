from itertools import combinations

n = int(input())
l = sorted(map(int, input().split()))

comb = list(combinations(l, 2))
result = 0
for cursor in comb:
    result = max(result, cursor[0] ^ cursor[1])

print(result)
