N = int(input())

A = list(map(int, input().split()))

increase = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)

decrease = [1 for i in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(N)]
for i in range(N):
    result[i] = increase[i] + decrease[i]-1

print(max(result))