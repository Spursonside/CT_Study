N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

ranking = [1 for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            ranking[i] += 1
        elif data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            ranking[j] += 1

for i in range(N):
    print(ranking[i], end = ' ')