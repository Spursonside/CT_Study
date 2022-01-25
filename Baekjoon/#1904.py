N = int(input())
if N == 1:
    cnt = 1

elif N == 2:
    cnt = 2

elif N > 2:
    dp = [0 for i in range(N)]
    dp[0] = 1
    dp[1] = 2
    for i in range(N-2):
        dp[i+2] = (dp[i+1] + dp[i]) % 15746
    cnt = dp[N-1]

print(cnt)
