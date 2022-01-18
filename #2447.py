def star(n, x, y):
    if n == 1:
        cord[y][x] = '*'
    else:
        nn = n // 3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx!= 1:
                    star(nn, x + dx * nn, y + dy * nn)


N = int(input())
cord = [[' ' for i in range(N)] for j in range(N)]
star(N, 0, 0)
for k in cord:
    print(''.join(k))