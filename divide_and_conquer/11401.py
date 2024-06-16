N, K = map(int, input().split())
P = 1000000007


def factorial(num, mod):
    n = 1
    for i in range(2, num + 1):
        n = n * i % P
    return n


def power(num, p, mod):
    if p == 1:
        return num % mod

    if p % 2:
        return ((power(num, p // 2, mod) ** 2) * num) % mod
    else:
        return (power(num, p // 2, mod) ** 2) % mod

print(factorial(N, P) * power((factorial(N - K, P) * factorial(K, P)), P - 2, P) % P)