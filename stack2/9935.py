S = input().strip()
target = input().strip()

stack = []
target_len = len(target)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-target_len:]) == target:
        for j in range(target_len):
            stack.pop()

if stack:
    print("".join(stack[:]))
    
else:
    print("FRULA")
