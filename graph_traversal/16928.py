from collections import deque

N, M = map(int, input().split())  # 사다리 수, 뱀 수

board = [0] * 101
visited = [False] * 101

ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v


def bfs(start):
    q = deque()
    q.append(start)

    visited[start] = True

    while q:
        cur = q.popleft()

        for i in range(1, 7):
            next = cur + i

            if 0 < next <= 100 and not visited[next]:
                if next in ladder:
                    next = ladder[next]

                if next in snake:
                    next = snake[next]

                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[cur] + 1


bfs(1)
print(board[100])