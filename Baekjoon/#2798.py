from itertools import permutations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

comb = list(permutations(numbers, 3))

sums = []
for c in comb:
    if sum(c) <= M:
        sums.append(sum(c))

print(max(sums))