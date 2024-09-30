n = int(input())

data = []

for i in range(n):
    [name, height, weight] = input().split()
    data.append([name, int(height), int(weight)])

data.sort(key=lambda x: (x[1], -x[2]))

for i in data:
    print('{} {} {}'.format(i[0], i[1], i[2]))