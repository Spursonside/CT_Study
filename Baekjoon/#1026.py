N = int(input())
A, B = [0 for i in range(N)], [0 for i in range(N)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
sum = 0
for i in range(N):
    mul = A[i] * B[i]
    sum = mul + sum
print(sum)
