N = int(input())
graph = [list(map(int, input())) for _ in range(N)]


def dfs(x, y, N):
    check = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = N // 2
        dfs(x, y, n)  # 오른쪽 위
        dfs(x, y + n, n)  # 왼쪽 위
        dfs(x + n, y, n)  # 오른쪽 아래
        dfs(x + n, y + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dfs(0, 0, N)