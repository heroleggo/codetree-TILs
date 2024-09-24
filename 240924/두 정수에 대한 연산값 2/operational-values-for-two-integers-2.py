def calc(a, b):
    if a > b:
        return a * 2,  b + 10
    else:
        return a + 10, b * 2

[n, m] = [int(x) for x in input().split()]

n, m = calc(n, m)

print('{} {}'.format(n, m))