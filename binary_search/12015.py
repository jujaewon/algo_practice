from bisect import bisect_left

N = int(input())
A = [*map(int, input().split())]

first = [A[0]]

for i in A:
    if first[-1] < i:
        first.append(i)
    else:
        idx = bisect_left(first, i)
        first[idx] = i

print(len(first))