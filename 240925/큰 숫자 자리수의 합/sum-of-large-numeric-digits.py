[a, b, c] = [int(x) for x in input().split()]

k = a * b * c

def s(data, n):
    return int(data[0]) if n == 0 else int(data[n]) + s(data, n - 1)

print(s(str(k), len(str(k)) - 1))