def solution(w,h):
    g = gcf(w, h)
    if g == 1:
        answer = w * h - (w + h - 1)
    else:
        answer = w * h - ((w + h) - g)

    return answer

def gcf(num1, num2):
    tmp = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            tmp.append(i)

    return max(tmp)