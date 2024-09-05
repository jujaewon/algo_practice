import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
edges = []
dist = [INF] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))


def bf(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            start_city = edges[j][0]
            next_city = edges[j][1]
            time = edges[j][2]
            if dist[start_city] != INF and dist[next_city] > time + dist[start_city]:
                dist[next_city] = dist[start_city] + time
                if i == N - 1:
                    return True
    return False


n_c = bf(1)

if n_c:
    print("-1")
else:
    for i in range(2, N + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
