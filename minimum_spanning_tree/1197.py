from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def prim(start, weight):
    visit = [0] * (V + 1)
    q = [[weight, start]]
    ans = 0
    cnt = 0
    while cnt < V:
        k, v = heappop(q)
        if visit[v]:
            continue
        visit[v] = 1
        ans += k
        cnt += 1
        for u, w in graph[v]:
            heappush(q, [w, u])
    return ans


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

print(prim(1, 0))
