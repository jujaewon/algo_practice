import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V = int(input())  # 정점의 개수
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    tree = list(map(int, input().split()))
    for i in range(1, len(tree) // 2):
        graph[tree[0]].append((tree[2 * i - 1], tree[2 * i]))


# BFS 함수
def bfs(x):
    q = deque([x])
    visited[x] = True

    while q:
        now = q.popleft()
        for i, w in graph[now]:
            if not visited[i]:
                q.append((i))
                visited[i] = True
                distance[i] = distance[now] + w


visited = [False] * (V + 1)
distance = [0] * (V + 1)
bfs(1)

max_distance = max(distance)  # 최장 거리
max_node = distance.index(max_distance)  # 해당 노드

visited = [False] * (V + 1)
distance = [0] * (V + 1)
bfs(max_node)

print(max(distance))