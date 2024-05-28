n = int(input())

arr = []
for i in range(n):
    [a, b] = map(int, input().split())
    arr.append([b, a])

s_arr = sorted(arr)

for i in range(n):
    print(s_arr[i][1], s_arr[i][0])