def triple_step(n):
    dp = []
    dp[0] = 0
    dp[1] = 1
    dp[2] = dp[0] + dp[1] + 1 + 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + 3

    return dp[n]

