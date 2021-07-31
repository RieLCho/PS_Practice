def rec(_n, _k):
    if _k == 0 or _n == _k:
        return 1
    return rec(_n - 1, _k) + rec(_n - 1, _k - 1)

n, k = map(int, input().split())
print(rec(n, k))
