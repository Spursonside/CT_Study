N, K = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, input().split())))
P = [[0]*(N + 1) for _ in range(K + 1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if items[i][0] <= w:
            P[w][i] = max(items[i][1] + (P[(w - items[i][0])][i - 1]), P[w][i - 1])
        else: P[w][i] = P[w][i - 1]

print(P[K][N])