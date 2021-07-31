from sys import stdin
input = stdin.readline
counter = 0
n, m = map(int, input().split())
listen = [input().rstrip() for _ in range(n)]
see = [input().rstrip() for _ in range(m)]
listenAndSee = set(listen) & set(see)

print(len(listenAndSee))
for cursor in sorted(listenAndSee):
    print(cursor)