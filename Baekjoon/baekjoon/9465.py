T = int(input())
for testCase in range(T):
    n = int(input())
    arr = [[0 for i in range(n+1)] for j in range(2)]
    dp = [[0 for i in range(n+1)] for j in range(2)]
    for i in range(2):
        temp = list(map(int, input().split()))
        for j in range(1, n+1, 1):
            arr[i][j] = temp[j-1]
    dp[0][0] = 0
    dp[1][0] = 0
    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]

    for i in range(2, n+1, 1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

    print(max(dp[0][n], dp[1][n]))

