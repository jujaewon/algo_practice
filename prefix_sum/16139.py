import sys

input = sys.stdin.readline

S = list(input().rstrip())
q = int(input().rstrip())

arr = [[0] * len(S) for _ in range(26)]

for i in range(len(S)):
    arr[ord(S[i]) - ord('a')][i] += 1

for i in range(26):
    for j in range(1, len(S)):
        arr[i][j] += arr[i][j - 1]

for i in range(q):
    a, l, r = input().split()
    cnt = arr[ord(a) - ord('a')][int(r)] - arr[ord(a) - ord('a')][int(l)]

    if S[int(l)] == a:
        cnt += 1

    print(cnt)