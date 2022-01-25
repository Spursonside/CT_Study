N = int(input())
dp = [[0 for y in range(0, 10)] for x in range(N)]
dp[0] = [1 for i in range(0, 10)]
dp[0][0] = 0

for i in range(1, N):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

if N == 1:
    print(9)
else:
    print(sum(dp[N-1]) % 1000000000)
