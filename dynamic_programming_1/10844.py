N = int(input())

# DPtable 초기화
step = [[0] * 10 for _ in range(N)]

# 1층 초값 설정
step[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 점화식 구현
for n in range(1, N):
    step[n][0] = step[n - 1][1]  
    step[n][9] = step[n - 1][8]

    for k in range(1, 9):  
        step[n][k] = step[n - 1][k - 1] + step[n - 1][k + 1]

print(sum(step[N - 1]) % 1000000000)
