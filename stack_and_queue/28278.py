import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    num = list(map(int, input().split()))

    if num[0] == 1:
        stack.append(num[1])

    elif num[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif num[0] == 3:
        print(len(stack))

    elif num[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif num[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)