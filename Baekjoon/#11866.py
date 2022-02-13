from collections import deque
N, K = map(int, input().split())

D = deque([_ for _ in range(1, N + 1)])
ans = []
for i in range(N):
    D.rotate(-K + 1)
    ans.append(str(D.popleft()))

print("<",', '.join(ans),">", sep="")