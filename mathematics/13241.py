A, B = map(int, input().split())
min_val = A*B

while B:
    if A > B:
        A, B = B, A
    B %= A

print(min_val//A)