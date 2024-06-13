import sys

n, m = map(int, sys.stdin.readline().split())
result = [0]
result += list(map(int, input().split()))

for i, num in enumerate(result):

    if i > 0:
        result[i] = result[i - 1] + num

# 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(result[j] - result[i - 1])