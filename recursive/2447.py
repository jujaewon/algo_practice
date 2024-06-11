def append_star(LEN):
    if LEN == 1:
        return ['*']

    stars = append_star(LEN // 3)
    lst = []

    for s in stars:
        lst.append(s * 3)
    for s in stars:
        lst.append(s + ' ' * (LEN // 3) + s)
    for s in stars:
        lst.append(s * 3)
    return lst


N = int(input().strip())
print('\n'.join(append_star(N)))
