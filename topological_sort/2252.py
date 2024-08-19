import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
sequence = [0 for _ in range(N+1)]
queue = deque()
answer = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    sequence[B] += 1

for i in range(1, N+1):
    if sequence[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        sequence[i] -= 1
        if sequence[i] == 0:
            queue.append(i)

print(*answer)