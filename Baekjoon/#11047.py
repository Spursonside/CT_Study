N, K = map(int, input().split())
coins = []
rest = K
cnt = 0
for _ in range(N):
    coins.append(int(input()))

for i in range(N-1, -1, -1):
    if rest >= coins[i]:
        cnt = cnt + (rest // coins[i])
        rest = rest % coins[i]
        if rest == 0:
            break

print(cnt)
