num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    A = num
    B = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    A = line - num + 1
    B = num

print(f'{A}/{B}')