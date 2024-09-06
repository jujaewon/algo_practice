import sys
from itertools import combinations

N, C = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

a, b = lst[:N // 2], lst[N // 2:]
A, B = [], []

cnt = 1

for i in range(1, len(a) + 1):
    for j in combinations(a, i):
        a_sum = sum(j)
        if a_sum <= C:
            A.append(a_sum)

for i in range(1, len(b) + 1):
    for j in combinations(b, i):
        b_sum = sum(j)
        if b_sum <= C:
            B.append(b_sum)
B.sort()

for i in A:
    start, end = 0, len(B)
    while start < end:
        mid = (start + end) // 2
        if i + B[mid] <= C:
            start = mid + 1
        else:
            end = mid
    cnt += end
print(len(A) + len(B) + cnt)
