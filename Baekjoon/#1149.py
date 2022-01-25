"""
for i in range(A):
    for j in range(i):
        if Ai[i] > Ai[j]:
            cnt[i] = max(cnt[i],cnt[j]+1)
"""
N = int(input())
H = [[0 for i in range(3)] for j in range(N)]

for i in range(N):
    H[i] = list(map(int, input().split()))

for i in range(1, len(H)):
    H[i][0] = min(H[i-1][1], H[i-1][2]) + H[i][0]
    H[i][1] = min(H[i-1][0], H[i-1][2]) + H[i][1]
    H[i][2] = min(H[i-1][1], H[i-1][0]) + H[i][2]

print(min(H[N-1][0], H[N-1][1], H[N-1][2]))
