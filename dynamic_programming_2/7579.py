N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
length = sum(cost)+1
dp = [[0 for _ in range(length)] for _ in range(N+1)]
result = 10001

for i in range(1, N+1):
    ci, mi = cost[i], memory[i]
    for j in range(length):
        dp[i][j] = dp[i-1][j]
    for j in range(ci, length):
        dp[i][j] = max(dp[i-1][j-ci] + mi, dp[i][j])
        if dp[i][j] >= M:
            result = min(result, j)

print(result)