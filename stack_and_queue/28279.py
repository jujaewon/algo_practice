import sys
from collections import deque

N = int(input())
queue = deque([])

for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().strip().split()))

    if cmd[0] == 1:
        queue.appendleft(cmd[1])

    elif cmd[0] == 2:
        queue.append(cmd[1])

    elif cmd[0] == 3:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif cmd[0] == 4:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif cmd[0] == 5:
        print(len(queue))

    elif cmd[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 7:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
