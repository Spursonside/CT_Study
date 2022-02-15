N = int(input())
Square = []
for _ in range(N):
    Square.append(list(map(int, input())))

def sol(x, y, n):
    tmp = Square[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != Square[i][j]:
                print("(", end = '')
                sol(x, y, n // 2)
                sol(x, y + n // 2, n // 2)
                sol(x + n // 2, y, n // 2)
                sol(x + n // 2, y + n // 2, n // 2)
                print(")", end = '')
                return

    if tmp == 0:
        print("0", end = '')
        return
    else:
        print("1", end = '')
        return

sol(0, 0, N)