[a, b] = list(map(int, input().split()))

print('{0:.2f}'.format(round((a + b) / (a - b), 2)))