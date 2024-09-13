import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

arr = []

while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def solution(A):
    if len(A) == 0:
        return

    left, right = [], []
    mid = A[0]
    for i in range(1, len(A)):
        if A[i] > mid:
            left = A[1:i]
            right = A[i:]
            break
    else:
        left = A[1:]

    solution(left)
    solution(right)
    print(mid)


solution(arr)