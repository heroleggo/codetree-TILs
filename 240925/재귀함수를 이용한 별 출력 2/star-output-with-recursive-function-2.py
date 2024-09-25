def p(a, n):
    if a == 0:
        return
    print(' '.join(["*"] * a))
    p(a - 1, n)
    print(' '.join(["*"] * a))

n = int(input())

p(n, n)