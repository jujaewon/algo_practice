import heapq

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start, size):
    distance = [float('inf')] * (size + 1)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
        for n, w in graph[node]:
            cost = dist + w

            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q, [cost, n])

    return distance


d1 = dijkstra(1, N)
d2 = dijkstra(v1, N)
d3 = dijkstra(v2, N)

result = min(d1[v2] + d2[N] + d3[v1], d1[v1] + d2[v2] + d3[N])

if result == float('inf'):
    print(-1)
else:
    print(result)
