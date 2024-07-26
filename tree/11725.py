from collections import deque

N = int(input())
graph = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0] * (N + 1)


def bfs():
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if ans[i] == 0:
                ans[i] = now
                queue.append(i)


bfs()
res = ans[2:]
for x in res:
    print(x)
