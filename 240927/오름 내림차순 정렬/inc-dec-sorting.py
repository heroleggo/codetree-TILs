n = int(input())
data = [int(x) for x in input().split()]

data.sort()

print(' '.join([str(x) for x in data]))

data.sort(reverse=True)

print(' '.join([str(x) for x in data]))