from collections import deque
import sys

T = int(sys.stdin.readline())

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == x_end and y == y_end:
            return chess[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and chess[nx][ny] == 0:
                q.append((nx, ny))
                chess[nx][ny] = chess[x][y] + 1


for _ in range(T):  # 테스트 케이스
    L = int(input())  # 한 변의 길이
    chess = [[0] * L for _ in range(L)]
    x_start, y_start = map(int, input().split())  
    x_end, y_end = map(int, input().split())  
    print(bfs(x_start, y_start))
