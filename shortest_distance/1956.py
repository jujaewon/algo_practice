V, E = map(int, input().split())
INF = int(1e9)

matrix = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = 1e9

for i in range(1, V+1):
    answer = min(answer, matrix[i][i])

if answer == 1e9:
    print(-1)
else:
    print(answer)


