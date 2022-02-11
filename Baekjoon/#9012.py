T = int(input())
ps = []
for i in range(T):
    ps.append(input())

ans = []

for p in range(len(ps)):
    tmp = 0
    for s in range(len(ps[p])):
        if ps[p][s] == "(":
            tmp += 1
        if ps[p][s] == ")":
            if tmp > 0:
                tmp -= 1
            else:
                ans.append("NO")
                break
    if tmp == 0 and len(ans) < p + 1:
        ans.append("YES")
    elif len(ans) < p + 1:
        ans.append("NO")

for a in ans:
    print(a)