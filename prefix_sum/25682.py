N, M, K = map(int, input().split())

board = [input() for _ in range(N)]

check_black = [[0 for _ in range(M+1)] for _ in range(N+1)]
check_white = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        # N, M과 각각의 합이 홀수, 짝수 여부
        if (i + j) % 2:
            if board[i][j] == 'B':
                check_black[i][j] = 1 + check_black[i-1][j] + check_black[i][j-1] - check_black[i-1][j-1]
                check_white[i][j] = 0 + check_white[i-1][j] + check_white[i][j-1] - check_white[i-1][j-1]
            else:
                check_black[i][j] = 0 + check_black[i-1][j] + check_black[i][j-1] - check_black[i-1][j-1]
                check_white[i][j] = 1 + check_white[i-1][j] + check_white[i][j-1] - check_white[i-1][j-1]
        else:
            if board[i][j] == 'B':
                check_black[i][j] = 0 + check_black[i-1][j] + check_black[i][j-1] - check_black[i-1][j-1]
                check_white[i][j] = 1 + check_white[i-1][j] + check_white[i][j-1] - check_white[i-1][j-1]
            else:
                check_black[i][j] = 1 + check_black[i-1][j] + check_black[i][j-1] - check_black[i-1][j-1]
                check_white[i][j] = 0 + check_white[i-1][j] + check_white[i][j-1] - check_white[i-1][j-1]

ans = 1e9
for i in range(N - K + 1):
    for j in range(M - K + 1):
        B_sub_sum = check_black[i+K-1][j+K-1] - check_black[i-1][j+K-1] - check_black[i+K-1][j-1] + check_black[i-1][j-1]
        W_sub_sum = check_white[i+K-1][j+K-1] - check_white[i-1][j+K-1] - check_white[i+K-1][j-1] + check_white[i-1][j-1]
        ans = min(ans, B_sub_sum, W_sub_sum)

print(ans)