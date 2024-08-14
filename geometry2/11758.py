plane = []
for _ in range(3):
    plane.append(list(map(int, input().split())))


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])


ans = ccw(plane[0], plane[1], plane[2])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
