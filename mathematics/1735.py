A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

A = A1*B2 + B1*A2
B = A2*B2
C = gcd(A, B)
print(A//C, B//C)