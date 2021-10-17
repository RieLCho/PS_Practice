a = list(map(int, input().split()))
target = max(a)
print(sum(list(map(lambda x: abs(x - target) if (x < target) else 0, a))))
