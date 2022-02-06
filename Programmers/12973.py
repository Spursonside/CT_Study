"""
나의 풀이, 반례가 있으나 못 찾고 효율성 테스트도 통과 못 함
A = input()
i = 0
while A != "":
    try:
        if A[i] == A[i + 1]:
            A = A.replace(A[i], "", 2)
            i = 0
        else:
            i += 1
    except:
        break
"""

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0