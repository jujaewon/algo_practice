import sys

N, M = map(int, sys.stdin.readline().split())

d = {}
for i in range(N):
    x = sys.stdin.readline().strip()

    if len(x) >= M:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

d = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in d:
    print(i[0])
