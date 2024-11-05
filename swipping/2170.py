import sys

input = sys.stdin.readline

N = int(input())
lines = []
ans = 0

for _ in range(N):
    lines.append(tuple(map(int, input().split())))

lines.sort()

start, end = lines[0]

for i in range(1, N):
    x, y = lines[i]

    if x <= end:
        end = max(y, end)
    else:
        ans += (end - start)
        start, end = x, y

ans += (end - start)
print(ans)
