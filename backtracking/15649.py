N, M = list(map(int, input().split()))

res = []


def backtracking(num):
    if len(res) == M:
        print(*res)
        return

    for i in range(1, N + 1):
        if i not in res:
            res.append(i)
            backtracking(num)
            res.pop()


backtracking(1)

