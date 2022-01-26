from itertools import permutations

def solution(expression):
    answer = 0
    op = ["+", "-", "*"]
    operations = list(permutations(op, len(op)))

    ans = [0 for _ in range(len(op))]

    for oper in operations:
        ans.append(abs(int(calc(oper, 0, expression))))

    answer = max(ans)

    return answer

def calc(operation, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if operation[seq] == "*":
            splitted = exp.split("*")
            tmp = []
            for s in splitted:
                tmp.append(calc(operation, seq + 1, s))
            return str(eval("*".join(tmp)))
        if operation[seq] == "+":
            splitted = exp.split("+")
            tmp = []
            for s in splitted:
                tmp.append(calc(operation, seq + 1, s))
            return str(eval("+".join(tmp)))
        if operation[seq] == "-":
            splitted = exp.split("-")
            tmp = []
            for s in splitted:
                tmp.append(calc(operation, seq + 1, s))
            return str(eval("-".join(tmp)))


print(solution(input()))