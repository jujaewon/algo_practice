N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))

res = []
order = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == order:
        res.append(arr[i])
        order -= 1

res.reverse()
print(*res)
