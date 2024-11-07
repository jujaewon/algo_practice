from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ""))
    visit = [False] * 10000

    while q:
        num1, path = q.popleft()
        visit[num1] = True
        if num1 == B:
            print(path)
            break

        num2 = (2 * num1) % 10000
        if not visit[num2]:
            q.append((num2, path + "D"))
            visit[num2] = True

        num2 = (num1 - 1) % 10000
        if not visit[num2]:
            q.append((num2, path + "S"))
            visit[num2] = True

        num2 = (10 * num1 + (num1 // 1000)) % 10000
        if not visit[num2]:
            q.append((num2, path + "L"))
            visit[num2] = True

        num2 = (num1 // 10 + (num1 % 10) * 1000) % 10000
        if not visit[num2]:
            q.append((num2, path + "R"))
            visit[num2] = True
