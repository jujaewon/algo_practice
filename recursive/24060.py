def merge_sort(l):
    if len(l) == 1:
        return l

    mid = (len(l) + 1) // 2

    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    i, j = 0, 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        lst.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        lst.append(right[j])
        ans.append(right[j])
        j += 1

    return lst


N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = []
merge_sort(A)

if len(ans) >= K:
    print(ans[K - 1])
else:
    print(-1)