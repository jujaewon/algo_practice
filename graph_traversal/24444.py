import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[R] = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 1

def bfs(v):
    global count
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        for i in sorted(graph[now]):
            if visited[i] == 0:
                count += 1
                visited[i] = count
                q.append(i)

bfs(R)

for i in range(1, N+1):
    print(visited[i])



