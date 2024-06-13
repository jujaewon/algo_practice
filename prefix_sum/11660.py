N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

sum_dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + array[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    ans = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]
    print(ans)
