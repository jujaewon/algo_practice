from collections import defaultdict

N = int(input())
dance = defaultdict(bool)
dance['ChongChong'] = True
cnt = 1

for _ in range(N):

    A, B = input().split()

    if dance[A]:
        if not dance[B]:
            dance[B] = True
            cnt += 1
    elif dance[B]:
        dance[A] = True
        cnt += 1

print(cnt)