N, C = map(int, input().split())

array = []
for i in range(N):
    array.append(int(input()))

array.sort()


def binary_search(array, left, right):
    while left <= right:
        mid = (left + right) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global answer
            left = mid + 1
            answer = mid
        else:
            right = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)