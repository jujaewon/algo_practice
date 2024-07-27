N = int(input())
shape = []

for _ in range(N):
    shape.append(list(map(int, input().split(' '))))
shape.append(shape[0])

answer = 0
for i in range(N):
    answer += shape[i][0] * shape[i+1][1] - shape[i+1][0] * shape[i][1]

print(abs(answer)/2)