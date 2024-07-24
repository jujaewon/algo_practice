from collections import Counter

N = int(input())
A = list(map(int, input().split()))

lst = [-1] * N
stack = []
fa = Counter(A)

for i in range(N):
    while stack and fa[A[stack[-1]]] < fa[A[i]]:
        lst[stack.pop()] = A[i]
    stack.append(i)

print(*lst)
