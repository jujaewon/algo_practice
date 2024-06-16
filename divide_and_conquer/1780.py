N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def cutting(x, y, N) :
  number = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if number != paper[i][j] :
        cutting(x, y, N // 3)
        cutting(x, y + N // 3, N // 3)
        cutting(x, y + 2 * N // 3, N // 3)
        cutting(x + N // 3, y, N // 3)
        cutting(x + N // 3, y+ N // 3, N // 3)
        cutting(x + N // 3, y + 2 * N // 3, N // 3)
        cutting(x + 2 * N // 3, y, N // 3)
        cutting(x + 2 * N // 3, y + N // 3, N // 3)
        cutting(x + 2 * N // 3, y + 2 * N // 3, N // 3)
        return
  if number == 0 :
    result.append(0)
  elif number == -1:
    result.append(-1)
  else :
    result.append(1)


cutting(0,0,N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))