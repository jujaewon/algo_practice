n = int(input())

lst = []
for i in str(n):
    lst.append(int(i))

lst.sort(reverse=True)  # 내림차순

for i in lst:
    print(i, end='')