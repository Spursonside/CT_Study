T = int(input())
A, B, C = 0, 0, 0
if T%10 != 0:
    print(-1)
elif T == 0:
    print(0)
elif T >= 300:
    A = T//300
    T = T - 300*A
    if T >= 60:
        B = T//60
        T = T - 60*B
        C = T//10
    else:
        C = T//10
    print(A, B, C)
elif T < 300 and T >= 60:
    B = T//60
    T = T-60*B
    C = T//10
    print(A, B, C)
else:
    C = T//10
    print(A, B, C)
