n = int(input())

originalData = list(map(int, input().split()))

data = []

for idx, val in enumerate(originalData):
    data.append([val, idx + 1])

data.sort(key=lambda x: (x[0], x[1]))

for idx, _ in enumerate(data):
    data[idx].append(idx + 1)

data.sort(key=lambda x: (x[1]))

print(' '.join([str(x[2]) for x in data]))