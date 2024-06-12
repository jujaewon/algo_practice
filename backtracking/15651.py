N, M = list(map(int, input().split()))

res = []


def backtracking():
    if len(res) == M:
        print(*res)
        return

    for i in range(1, N + 1):

        res.append(i)
        backtracking()
        res.pop()


backtracking()
