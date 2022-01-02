N, L = map(int, input().split())
leak = [0 for i in range(N)]
leak = list(map(int, input().split()))
leak.sort()
tape = 0
Ntape = 0
for i in leak:
    if tape < i:
        Ntape = Ntape + 1
        tape = i + L - 1
print(Ntape)
