N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
    if num[-1] == 0:
        num.pop()
        num.pop()

print(sum(num))