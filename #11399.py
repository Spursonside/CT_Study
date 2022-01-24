N = int(input())
P = list(map(int, input().split()))

P.sort()

s = [P[0]]

for i in range(1, N):
    s.append(s[i - 1] + P[i])

print(sum(s))