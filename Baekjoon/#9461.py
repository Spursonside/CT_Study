T = int(input())
N = [0 for i in range(T)]
for i in range(T):
    N[i] = int(input())

P = [0 for i in range(100)]
P[0] = 1
P[1] = 1
P[2] = 1

for i in range(97):
    P[i+3] = P[i] + P[i+1]

for i in range(T):
    print(P[N[i]-1])11
