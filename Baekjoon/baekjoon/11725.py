import sys

n = int(input())
trees = [[] for i in range(n + 1)]
parents = [0 for i in range(n + 1)]
sys.setrecursionlimit(10**5)
for _ in range(n - 1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

def dfs(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, tree, parent)


dfs(1, trees, parents)

for i in range(2, n + 1):
    print(parents[i])
