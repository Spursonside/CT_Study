A = input()
length = []


for j in range(1, len(A)//2 + 2):
    a = 0
    b = False
    tmp = A[:j]
    for i in range(j, len(A) + j, j):
        if A[i:i+j] == tmp:
            b = True
        else:
            if b:
                a += 1
            a += len(tmp)
            tmp = A[i:i+j]
            b = False
    length.append(a)

