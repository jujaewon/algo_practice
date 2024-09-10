from collections import deque

N = int(input())
q = deque()
q.append([N])
ans = []

while q:
    a = q.popleft()
    X = a[0]
    if X == 1:
        ans = a
        break

    if X % 3 == 0:
        q.append([X // 3] + a)

    if X % 2 == 0:
        q.append([X // 2] + a)

    q.append([X - 1] + a)

print(len(ans) - 1)
print(*ans[::-1])
