n = int(input())

data = []

for i in range(n):
    data.append(input().split())

data.sort(key=lambda x: (int(x[1]) + int(x[2]) + int(x[3])))

for i in data:
    print(' '.join(i))