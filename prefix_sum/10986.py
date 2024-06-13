N, M = map(int, input().split())
A = list(map(int, input().split()))

r = [0] * M

prefixSum = 0
for i in range(N):
    prefixSum += A[i]
    r[prefixSum % M] += 1

ans = r[0]

for i in range(M):
    ans += r[i] * (r[i]-1) // 2
print(ans)
