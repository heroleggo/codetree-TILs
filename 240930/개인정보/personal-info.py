data = []

for i in range(5):
    [name, height, weight] = input().split()
    data.append([name, height, weight])

data.sort(key=lambda x: x[0])

print('name')
for i in data:
    print('{} {} {}'.format(i[0], i[1], format(float(i[2]), '.1f')))

data.sort(key=lambda x: -int(x[1]))

print()
print('height')
for i in data:
    print('{} {} {}'.format(i[0], i[1], format(float(i[2]), '.1f')))