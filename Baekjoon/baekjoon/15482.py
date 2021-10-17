string1 = input()
string2 = input()

dp = [0 for _ in range(1001)]
for i in range(len(string1)):
    dp_max = 0
    for j in range(len(string2)):
        if dp_max < dp[j]:
            dp_max = dp[j]
        elif string1[i] == string2[j]:
            dp[j] = dp_max + 1

print(max(dp))