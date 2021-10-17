N = int(input())
s, g, p, d = list(map(int, input().split()))
rank = input()

dp = [0 for i in range(N)]
guideline = {'B': [0, s - 1], 'S': [s, g - 1], 'G': [g, p - 1], 'P': [p, d - 1], 'D': [d, d * 2]}

if rank[0] == 'D':
    dp[0] = d
else:
    dp[0] = guideline[rank[0]][1]

for i, r in enumerate(rank[1:]):
    i = i + 1

    if r == 'D':
        dp[i] = d
        continue

    val = dp[i - 1] + dp[i]
    if val < guideline[r][1]:
        dp[i] = guideline[r][1] - dp[i - 1]
    elif val > guideline[r][1]:
        dp[i] = 0
        dp[i - 1] = guideline[r][1]
        for ii in range(i - 1, 0, -1):
            if dp[ii] + dp[ii - 1] < guideline[rank[ii]][0]:
                dp[ii - 1] = guideline[rank[ii]][0] - dp[ii]
            elif dp[ii] + dp[ii - 1] > guideline[rank[ii]][1]:
                dp[ii - 1] = guideline[rank[ii]][1] - dp[ii]
            else:
                break
print(sum(dp))