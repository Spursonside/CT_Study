def find(target):
    start, end = 0, len(stack)
    while start < end:
        mid = (start + end) // 2
        if stack[mid] < target:
            start = mid + 1
        else: end = mid
    return end

N = int(input())
A = list(map(int, input().split()))
stack = []

for a in A:
    if not stack:
        stack.append(a)
        continue
    if stack[-1] < a:
        stack.append(a)
    else: stack[find(a)] = a

print(len(stack))