N = int(input())

def thr(n):
    tmp = ''

    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 0:
            mod = 4
            n -= 1
        tmp += str(mod)

    return tmp[::-1]

a = thr(N)