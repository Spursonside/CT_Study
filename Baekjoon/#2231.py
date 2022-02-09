N = int(input())

def digits_sum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

answer = 0

for i in range(N):
    if i + digits_sum(i) == N:
        answer = i
        break

print(answer)
