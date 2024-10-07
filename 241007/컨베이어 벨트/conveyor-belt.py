[n, t] = list(map(int, input().split()))

data = []

for i in range(2):
    data.extend(list(map(int, input().split())))

belt = data[0]

second = t % (n * 2)

l = len(data)

for i in range(second):
    tmp = data[l - 1]
    for j in range(l - 1, 0, -1):
        data[j] = data[j - 1]
    data[0] = tmp

result = [data[0:n], data[n:]]

for i in result:
    print(' '.join([str(x) for x in i]))