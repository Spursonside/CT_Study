from sys import stdin
import heapq

N = int(stdin.readline())
leftheap, rightheap = [], []

for i in range(N):
    n = int(stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -n)
    else:
        heapq.heappush(rightheap, n)
    if rightheap and -leftheap[0] > rightheap[0]:
        l = -heapq.heappop(leftheap)
        r = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -r)
        heapq.heappush(rightheap, l)

    print(-leftheap[0])