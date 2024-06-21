n = int(input())

wine = [[] for _ in range(n)]

for i in range(0,n):
    wine[i] = int(input())

dp = [0] * n # i번째 줄까지에서 마실 수 있는 최대 포도주 양

dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(dp[1], wine[0]+wine[2], wine[1]+wine[2])
    
if n > 3:
    for i in range(3,n):
        # xoox의 경우 : dp[i-1]
        # ooxo의 경우 : dp[i-2]+arr[i]
        # oxoo의 경우 : dp[i-3]+arr[i-1]+arr[i]
        dp[i] = max(dp[i-1], dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])
print(dp[n-1])