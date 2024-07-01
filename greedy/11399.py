n = int(input())
lines = list(map(int, input().split()))

lines.sort()  
answer = 0  

for i in range(1, n+1):
    answer += sum(lines[0:i])
print(answer)  