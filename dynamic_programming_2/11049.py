N = int(input())
matrix = [tuple(map(int, input().split())) for i in range(N)]

dp = [[0] * N for i in range(N)]
for cnt in range(N - 1):
    for i in range(N - 1 - cnt):
        j = i + cnt + 1
        dp[i][j] = 2 ** 31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][-1])
