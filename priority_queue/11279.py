import heapq
import sys

heap = []
N = int(input())

for i in range(N):
    num = int(sys.stdin.readline()) * -1
    if num == 0:
        print(heapq.heappop(heap) * -1 if heap else 0)
    else:
        heapq.heappush(heap, num)