from collections import deque
N = int(input())
Q = deque([i for i in range(1, N + 1)])

n = 1
while len(Q) > 1:
    if n % 2 == 1:
        Q.popleft()
    elif n % 2 == 0:
        Q.append(Q.popleft())
    n += 1

print(Q[-1])