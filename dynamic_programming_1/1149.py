house = []
N = int(input())
for _ in range(N):
    house.append(list(map(int, input().split())))

for i in range(1, N):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[N-1]))
