N = int(input())
S = []
for i in range(N):
    S.append(int(input()))

stack = []
ans0 = []
ans1 = []
n = 1
for s in S:
    while n <= s:
        stack.append(n)
        ans0.append('+')
        n += 1
    ans0.append('-')
    ans1.append(stack.pop())

if ans1 == S:
    for i in range(len(ans0)):
        print(ans0[i])
else: print("NO")