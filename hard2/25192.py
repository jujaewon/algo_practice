N = int(input())
bear = set()
cnt = 0

for _ in range(N):
    user = input().strip()
    if user == 'ENTER':
        cnt += len(bear)
        bear = set()
    else:
        bear.add(user)

cnt += len(bear)
print(cnt)