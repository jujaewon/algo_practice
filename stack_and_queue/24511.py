import sys
from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())

C = list(map(int, input().split()))

queue = deque()

for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
else:
    if len(B) == 0:
        print(*C)
        sys.exit()
        
for i in range(M):
    # queStack 내부 가장 왼쪽에 수열의 값을 넣어준다.
    queue.appendleft(C[i])
    # queStack 마지막 자료를 pop 해주고 출력.
    print(queue.pop(), end=" ")