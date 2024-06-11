def hanoi(k, start, end):
    if k == 1:
        print(start, end)
        return

    hanoi(k - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    hanoi(k - 1, 6 - start - end, end)  # 3단계


K = int(input())
print(2 ** K - 1)
hanoi(K, 1, 3)