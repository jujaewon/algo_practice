import sys
sys.setrecursionlimit(10**9)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[R] = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 1

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visited[i])