N = int(input())
num = list(map(int, input().split()))
# 연산자
cal = list(map(int, input().split())) 

max_val = -1e9
min_val = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global max_val, min_val
    if depth == N:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return

    # 사칙연산자에 따라 사례 분류
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], cal[0], cal[1], cal[2], cal[3])
print(max_val)
print(min_val)
