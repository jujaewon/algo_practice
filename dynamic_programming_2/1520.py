import sys
sys.setrecursionlimit(10 ** 9)


# dfs 탐색
def dfs(x, y):

    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]


M, N = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(dfs(0, 0))
