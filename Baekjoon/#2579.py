N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
dp = [0 for i in range(N)]

if N >= 1:
    dp[N-1] = A[N-1]
if N >= 2:
    dp[N-2] = A[N-1] + A[N-2]
if N >= 3:
    dp[N-3] = A[N-3] + A[N-1]
if N >= 4:
    for i in range(N, 3, -1):
        dp[i-4] = max(dp[i-1] + A[i-3], dp[i-2]) + A[i-4]

if N == 1:
    print(dp[0])
else:
    print(max(dp[0], dp[1]))
