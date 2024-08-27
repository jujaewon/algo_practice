from collections import deque


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    while q:
        x, y, c = q.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 and c == 0:
                visit[nx][ny][1] = visit[x][y][0] + 1
                q.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visit[nx][ny][c] == 0:
                visit[nx][ny][c] = visit[x][y][c] + 1
                q.append((nx, ny, c))
    return -1


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(bfs(0, 0, 0))
