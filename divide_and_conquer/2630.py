N = int(input())

color_paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def cutting(x, y, N) :
  color = color_paper[x][y]
  for i in range(x, x + N) :
    for j in range(y, y + N) :
      if color != color_paper[i][j] :
        cutting(x, y, N // 2)
        cutting(x, y + N // 2, N // 2)
        cutting(x + N // 2, y, N // 2)
        cutting(x + N // 2, y + N // 2, N // 2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


cutting(0,0,N)
print(result.count(0))
print(result.count(1))