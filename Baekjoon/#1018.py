N, M = map(int, input().split())

board = []
for n in range(N):
    board.append(input())
cnts = []

for i in range(N - 7):
    for j in range(M - 7):
        cnt = [0, 0]
        chess = []
        for _ in range(i, i + 8):
            chess.append(board[_][j:j + 8])

        for x in range(8):
            for y in range(8):
                if (x % 2) == 1 and (y % 2) == 1:
                    if chess[x][y] != 'W':
                        cnt[0] += 1
                    if chess[x][y] != 'B':
                        cnt[1] += 1
                if (x % 2) == 0 and (y % 2) == 0:
                    if chess[x][y] != 'W':
                        cnt[0] += 1
                    if chess[x][y] != 'B':
                        cnt[1] += 1
                if (x % 2) == 1 and (y % 2) == 0:
                    if chess[x][y] != 'B':
                        cnt[0] += 1
                    if chess[x][y] != 'W':
                        cnt[1] += 1
                if (x % 2) == 0 and (y % 2) == 1:
                    if chess[x][y] != 'B':
                        cnt[0] += 1
                    if chess[x][y] != 'W':
                        cnt[1] += 1
        cnts.append(min(cnt))

print(min(cnts))