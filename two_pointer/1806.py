N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0 
cnt = 0 
min_length = 1e9 

while True:
    if cnt >= S:
        min_length = min(min_length, right - left)
        cnt -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        cnt += arr[right]
        right += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)