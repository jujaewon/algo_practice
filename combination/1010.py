T = int(input())

for _ in range(T):

    N, K = map(int, input().split())

    n = 1

    for num1 in range(N, 0, -1):
        n *= num1

    k = 1

    for num2 in range(K, K-N, -1):
        k *= num2

    result = k // n

    print(result)
