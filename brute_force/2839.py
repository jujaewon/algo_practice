N = int(input())

if N % 5 == 0:  # 5으로 나눠떨어질 때
    print(N // 5)
else:
    P = 0
    while N > 0:
        N -= 3
        P += 1
        if N % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            P += N // 5
            print(P)
            break
        elif N == 1 or N == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif N == 0:  # 3으로 나눠떨어질 때
            print(P)
            break