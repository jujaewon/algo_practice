N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
targets = list(map(int, input().split()))


def binary(target):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target:
            return True

        if target < num_list[mid]:
            right = mid-1
        elif target > num_list[mid]:
            left = mid + 1


for i in range(M):
    if binary(targets[i]):
        print(1)
    else:
        print(0)