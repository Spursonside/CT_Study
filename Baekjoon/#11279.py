from sys import stdin
import heapq

N = int(stdin.readline())
arr = []
for i in range(N):
    n = int(stdin.readline())
    if n != 0:
        heapq.heappush(arr, (-n, n))
    elif n == 0:
        try:
            print(heapq.heappop(arr)[1])
        except: print(0)