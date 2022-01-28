from collections import deque

pro = deque(map(int, input().split()))
spd = deque(map(int, input().split()))

def solution(progresses, speeds):
    complete = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        cnt = 0

        for i in range(len(progresses)):
            tmp0 = progresses.popleft()
            tmp1 = speeds.popleft()
            if tmp0 >= 100:
                cnt += 1
            else:
                progresses.appendleft(tmp0)
                speeds.appendleft(tmp1)
        if cnt != 0:
            complete.append(cnt)
    answer = complete
    return answer

print(solution(pro, spd))