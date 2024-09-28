n = int(input())

data = list(map(int, input().split()))

tmp = []

result = []

for i in range(n):
    tmp.append(data[i])
    if i % 2 == 0: # even index -> odd order
        tmp.sort()
        result.append(str(tmp[(len(tmp) - 1) // 2]))

print(' '.join(result))