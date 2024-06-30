n = int(input())
lines = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()

for i in range(1, n):
    for j in range(0, i):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))