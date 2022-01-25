N = int(input())

time = []

for i in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:(x[0], x[1]))

memo = []

memo.append(time[0])

for i in range(1, N):
    if memo[-1][1] > time[i][1]:
        memo[-1] = time[i]
    elif memo[-1][1] <= time[i][0]:
        memo.append(time[i])

print(len(memo))
