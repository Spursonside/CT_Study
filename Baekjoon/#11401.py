import sys

def pow(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        return (pow(a, b//2, mod) ** 2) % mod
    else: return (pow(a, b//2, mod) ** 2 * a) % mod

N, K = map(int, sys.stdin.readline().split())
p = 1000000007

fact = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = (fact[N - K] * fact[K] % p)

print((A % p) * (pow(B, p - 2, p) % p) % p)