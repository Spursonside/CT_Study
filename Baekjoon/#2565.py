N = int(input())
line = []
for i in range(N):
    line.append(list(map(int, input().split())))
dp = [1 for _ in range(N)]
list.sort(line)

for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
