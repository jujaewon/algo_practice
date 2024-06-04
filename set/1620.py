n, m = map(int, input().split())

d = {}

for i in range(1, n + 1):
    j = input().rstrip()
    d[i] = j
    d[j] = i

for i in range(m):
    ans = input().rstrip()
    if ans.isdigit():
        print(d[int(ans)])
    else:
        print(d[ans])