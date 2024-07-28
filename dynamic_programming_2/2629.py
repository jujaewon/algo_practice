n, weight_lst = int(input()), list(map(int, input().split()))
m, check_weight_lst = int(input()), list(map(int, input().split()))

dp = [0]
for weight in weight_lst:
    tmp = []
    for i in dp:
        tmp.append(i + weight)
        tmp.append(abs(i - weight))
    dp = list(set((dp + tmp)))

for weight in check_weight_lst:
    if weight in dp:
        print('Y', end=' ')
    else:
        print('N', end=' ')
