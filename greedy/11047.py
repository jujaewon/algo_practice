N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))

coin = 0

coins.sort(reverse=True)

for i in range(N):
    coin += K // coins[i]
    K = K % coins[i]

print(coin)