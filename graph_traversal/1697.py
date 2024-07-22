from collections import deque

N, K = map(int, input().split())

INF = 10 ** 5
visited = [0] * (INF + 1)


def bfs(s):
    q = deque()
    q.append(s)

    while q:
        cur = q.popleft()
        if cur == K:
            return visited[K]
        for i in (cur + 1, cur - 1, cur * 2):
            if 0 <= i <= INF and not visited[i]:
                visited[i] = visited[cur] + 1
                q.append(i)


print(bfs(N))
