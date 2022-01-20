"""
시간초과
N = int(input())
A = list(map(int, input().split()))

dp = [min(A) for _ in range(N)]

for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += A[j]
        if dp[i] <= sum:
            dp[i] = sum

print(max(dp))
"""
N = int(input())
A = list(map(int, input().split()))
dp = []
dp.append(A[0])

for i in range(1, N):
    dp.append(max(dp[i - 1] + A[i], A[i]))

print(max(dp))