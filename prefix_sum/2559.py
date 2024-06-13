N, K = map(int, input().split())
a = list(map(int, input().split()))

result = []
result.append(sum(a[:K]))

for i in range(N - K):
    result.append(result[i] - a[i] + a[K + i])

print(max(result))