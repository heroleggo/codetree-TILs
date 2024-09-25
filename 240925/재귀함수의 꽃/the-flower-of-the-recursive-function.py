def p(a, n):
    if a == 0:
        return
    print(a, end=' ')
    p(a - 1, n)
    print(a, end=' ')

n = int(input())

p(n, n)