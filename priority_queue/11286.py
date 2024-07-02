import heapq
import sys

res = []
N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(res, (abs(num), num))
    else:
        if res:
            print(heapq.heappop(res)[1])
        else:
            print(0)
