def calc(a, b):
    if a > b:
        return a + 25, 2 * b
    else:
        return 2 * a, b + 25

[n, m] = [int(x) for x in input().split()]

n, m = calc(n, m)

print('{} {}'.format(n, m))