N = int(input())
N_list = map(int, input().split())

M = int(input())
M_list = map(int, input().split())

dic = {}

for i in M_list:
    dic[i] = 0

for j in N_list:
    if j in dic:
        dic[j] = 1

for k in dic:
    print(dic[k], end=' ')