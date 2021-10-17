L, P = map(int, input().split())
news = list(map(int, input().split()))
for paper in news:
    print(paper - L*P, end=' ')
    