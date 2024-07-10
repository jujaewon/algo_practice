N = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = N - 1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    base_val = arr[left]
    acid_val = arr[right]

    mix = base_val + acid_val

    if abs(mix) < answer:
        answer = abs(mix)
        final = [base_val, acid_val]
        if answer == 0:
            break
    if mix < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
