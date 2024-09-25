def p(a, n):
    if a == n:
        print("*" * n)
        return
    else:
        print("*" * a)
        p(a + 1, n)

n = int(input())

p(1, n)