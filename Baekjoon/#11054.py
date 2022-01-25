N = int(input())
A = list(map(int, input().split()))

u = [1 for _ in range(N)]
d = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            u[i] = max(u[i], u[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i - 1, -1):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)
ans = []
for i in range(N):
    ans.append(u[i] + d[i])

print(max(ans) - 1)
