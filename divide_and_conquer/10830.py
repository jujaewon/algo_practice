N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# 행렬 곱하기(A*A) 알고리즘
def mul(N, A, B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def cal(N, B, A):
    if B == 1:
        return A
    # 단순 2제곱일 경우
    elif B == 2:
        return mul(N, A, A)
    else:
        tmp = cal(N, B // 2, A)
        # B가 짝수일 경우 제곱수를 계속 곱하면 된다.
        # AAAA = ((A^2)^2)
        if B % 2 == 0:
            return mul(N, tmp, tmp)
        # B가 홀수일 경우 마지막에 A를 곱해줘야한다.
        # AAAAA = ((A^2)^2)*A
        else:
            return mul(N, mul(N, tmp, tmp), A)

result = cal(N, B, A)

for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
