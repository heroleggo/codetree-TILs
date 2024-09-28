n = int(input())

data = [int(x) for x in input().split()]

data.sort()

result = -1

for i in range(n):
    result = max(result, data[i] + data[2 * n - i - 1])

print(result)