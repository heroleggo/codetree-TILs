n = int(input())

data = []

for i in range(n):
    [h, w] = list(map(int, input().split()))
    data.append([h, w, i + 1])

data.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in data:
    print('{} {} {}'.format(i[0], i[1], i[2]))