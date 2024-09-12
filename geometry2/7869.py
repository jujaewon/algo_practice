import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())


def area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    r1_square = r1 * r1
    r2_square = r2 * r2
    if d > r2 + r1:  # 원이 겹치지 않음
        return 0
    elif d <= abs(r1 - r2) and r1 < r2:
        return math.pi * r1_square
    elif d <= abs(r1 - r2) and r1 >= r2:
        return math.pi * r2_square
    else:
        phi = (math.acos((r1_square + (d * d) - r2_square) / (2 * r1 * d))) * 2
        theta = (math.acos((r2_square + (d * d) - r1_square) / (2 * r2 * d))) * 2
        area1 = 0.5 * r2_square * (theta - math.sin(theta))
        area2 = 0.5 * r1_square * (phi - math.sin(phi))
        return area1 + area2


result = float(round(1000 * area(x1, y1, r1, x2, y2, r2)) / 1000)
print('%.3f' % result)
