def s(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + s(n - 1)

n = int(input())

print(s(n))