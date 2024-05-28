n = int(input())

arr = []
for i in range(n):
    [a, b] = map(int, input().split())
    arr.append([a, b])

s_arr = sorted(arr)

for i in range(n):
    print(s_arr[i][0], s_arr[i][1])