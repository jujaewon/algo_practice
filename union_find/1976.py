from collections import deque

N = int(input())
M = int(input())

city = []

for i in range(N):
    city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

def bfs(s, e):
    q = deque()
    q.append(s)
    visited = [False] * N
    visited[s] = True

    while q:
        current = q.popleft()

        if current == e:
            return True

        for i in range(N):
            if city[current][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return False

answer = True

for i in range(M-1):
    if plan[i] != plan[i+1]:
        if not bfs(plan[i]-1, plan[i+1]-1):
            answer = False
            break

if answer:
    print('YES')
else:
    print('NO')