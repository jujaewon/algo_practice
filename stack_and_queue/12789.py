N = int(input())
stack = []
cnt = 1

line = list(map(int, input().split()))
while line:
    if cnt == line[0]:
        cnt+=1
        line.pop(0)
    else:
        stack.append(line.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt+=1
        else:
            break

if len(stack)==0:
    print("Nice")
else:
    print("Sad")