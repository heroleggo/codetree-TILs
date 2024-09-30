n = int(input())

data = []

for i in range(n):
    [x, y] = list(map(int, input().split()))
    data.append([x, y, abs(x) + abs(y), i + 1])

data.sort(key=lambda x: (x[2], x[3]))

for i in data:
    print(i[3])