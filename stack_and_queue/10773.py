K = int(input())
stack = []

for _ in range(K):
    num = int(input())

    if num != 0:
        stack.append(num)

    else:
        if stack:
            stack.pop()

cnt = 0
if stack:
    for i in stack:
        cnt += i
    print(cnt)


else:
    print(0)