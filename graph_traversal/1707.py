import sys

sys.setrecursionlimit(10 ** 6)
K = int(input())


def dfs(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
    return True


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if visited[i] == 0:
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")
