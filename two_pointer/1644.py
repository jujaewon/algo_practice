import math
N = int(input())

if N == 1:
    print(0)
    exit(0)

arr = [True] * (N + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(N)+1)):
    if arr[i]:
        j = 2

        while (i * j) <= N:
            arr[i*j] = False
            j += 1

prime_list = []

for i in range(2, N + 1):
    if arr[i]:
        prime_list.append(i)

left = 0
right = 0
temp_prime_sum = prime_list[0]
count = 0

while left <= right:

    if temp_prime_sum > N:
        temp_prime_sum -= prime_list[left]
        left += 1
    else:
        if temp_prime_sum == N:
            count += 1
        right += 1
        if right == len(prime_list):
            break
        temp_prime_sum += prime_list[right]

print(count)