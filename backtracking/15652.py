N, M = list(map(int, input().split()))

res = []


def backtracking(num):
    if len(res) == M:
        print(*res)
        return

    for i in range(num, N + 1):

        res.append(i)
        backtracking(i)
        res.pop()


backtracking(1)
