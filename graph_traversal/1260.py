from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)


def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[v][i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if not visited2[i] and graph[v][i]:
                q.append(i)
                visited2[i] = True


dfs(V)
print()
bfs(V)
