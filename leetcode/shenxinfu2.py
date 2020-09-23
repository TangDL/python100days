
import sys

def helper(N, K):
    print(N, K)
    dp=[0] * (N+1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    flag = 0
    for i in range(3, N+1):
        if K==0:
            dp[i] = dp[i-1] + dp[i-2] +dp[i-3]
        elif K != 0 and (i-3) // K>=flag:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            flag += 1
        else:
            dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    nums = []
    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().strip().split())))

    res = []
    for i in range(n):
        res.append(helper(nums[i][0], nums[i][1]))
    for i in range(n):
        sys.stdout.write("%d" % res[i])
        if i != n-1:
            sys.stdout.write("\n")


