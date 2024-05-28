n = int(input())
arr = list(map(int, input().split()))

arr_second = sorted(list(set(arr)))
dic = {arr_second[i] : i for i in range(len(arr_second))}
for i in arr:
    print(dic[i], end = ' ')