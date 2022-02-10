N = int(input())

def finding_six(n):
    tmp = 1
    num = str(666)
    while tmp < n:
        num = str(int(num) + 1)
        if num.find('666') != -1:
            tmp += 1

    return num

print(finding_six(N))