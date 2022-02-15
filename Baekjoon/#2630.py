N = int(input())
Square = []
for _ in range(N):
    Square.append(list(map(int, input().split())))

ans = [0, 0]
def sol(x, y, n):
    tmp = Square[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tmp != Square[i][j]:
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x + n//2, y, n//2)
                sol(x + n//2, y + n//2, n//2)
                return
    if tmp == 0:
        ans[0] += 1
    else: ans[1] += 1

sol(0, 0, N)
print(ans[0])
print(ans[1])