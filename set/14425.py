N, M = map(int, input().split())

String = []
cnt = 0

for _ in range(N):
    word = input().strip()
    String.append(word)

for _ in range(M):
    target = input().strip()

    if target in String:
        cnt += 1

print(cnt)