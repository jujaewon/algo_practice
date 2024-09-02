import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
tree = [0 for _ in range(N + 1)]


def dfs(i):
    tree[i] = 1
    for j in graph[i]:
        if not tree[j]:
            dfs(j)
            tree[i] += tree[j]


for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R)

for _ in range(Q):
    print(tree[int(sys.stdin.readline())])
