MOD = 10**9 + 7

n, m, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]


dp[0][0] = 1
for i in range(1, n+1):
    dp[i][0] = m


for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = (dp[i-1][j] * (m-1) + dp[i-1][j-1] * m) % MOD

answer = sum(dp[n][1:k+1]) % MOD
print(answer)

