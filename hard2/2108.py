from collections import Counter

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

# 산술평균 - 다 더해서 / n
print(round(sum(lst) / n))

# 중앙값 - 오름차순 -> 중간값
lst.sort()
print(lst[n // 2])

# 최빈값 - 빈출
cnt_lst = Counter(lst).most_common()
if len(cnt_lst) > 1 and cnt_lst[0][1] == cnt_lst[1][1]:  # 최빈값 2개 이상
    print(cnt_lst[1][0])
else:
    print(cnt_lst[0][0])

# 범위 - 최댓값-최솟값
print(max(lst) - min(lst))