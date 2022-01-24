N = int(input())

time = []

for i in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:x[0])

memo = [[0, max(time, key = lambda x:x[1])]]

for i in range(N):
    if memo[-1][0] <= time[i][0] and memo[-1][1] >= time[i][1]:
        memo.append(time[i])
    if memo[-1][1] <= time[i][0]:
        memo.append(time[i])

print(len(memo)-1)
