n = int(input())

person = {}

for _  in range(n):
    name, check = map(str, input().split())
    if check == 'enter':
        person[name] = True
    else:
        del person[name]

names = sorted(person, reverse=True)

for name in names:
    print(name)