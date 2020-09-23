


def frog(N):
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


if __name__ == "__main__":
    res = frog(8)
    print(res)

