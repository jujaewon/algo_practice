N, M = map(int, input().split())

a=set()
b=set()
result =[]

for _ in range(N):
    a.add(input())
    
for _ in range(M):
    b.add(input())

for i in a :
    if i in b :
        result.append(i)
        
result.sort()
print(len(result))
for i in result :
    print(i)