[n, t] = list(map(int, input().split()))

data = []

for i in range(3):
    data.extend(input().split())

second = t % (n * 3)

l = len(data)

for i in range(second):
    tmp = data[l - 1]
    for j in range(l - 1, 0, -1):
        data[j] = data[j - 1]
    data[0] = tmp

for i in range(3):
    for j in range(n):
        print(data[i * 3 + j], end=' ')