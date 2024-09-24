def swap(a, b):
    a, b = b, a
    return a, b

[n, m] = [int(x) for x in input().split()]


n, m = swap(n, m)

print(n, m)