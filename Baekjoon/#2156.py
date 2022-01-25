N = int(input())
wine = []
dp = []
for i in range(N):
    wine.append(int(input()))

dp.append(wine[0])

if N >= 2:
    dp.append(dp[0] + wine[1])
if N >= 3:
    dp.append(max(wine[0] + wine[2], wine[1] + wine[2], dp[1]))
if N >= 4:
    for i in range(3, N):
        dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))

print(dp[N-1])
