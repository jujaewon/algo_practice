A_count, B_count = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

only_A = list(set(A)-set(B))
only_B = list(set(B)-set(A))
print(len(only_A) + len(only_B))