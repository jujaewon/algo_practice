from collections import deque

queue = deque()
result = []

N, K = map(int, input().split())

for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")
