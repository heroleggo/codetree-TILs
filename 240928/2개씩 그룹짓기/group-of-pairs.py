n = int(input())

data = [int(x) for x in input().split()]

data.sort()

sum1 = 0
sum2 = 0

for i in range(n * 2):
    if i % 2 == 0:
        sum1 += data[i]
    else:
        sum2 += data[i]

print(max(sum1, sum2))