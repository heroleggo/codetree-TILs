def p(n):
    if n == 0:
        return
    elif n == 1:
        print('{}'.format(n))
    else:
        print('{}'.format(n), end=' ')
        p(n - 1)

def pp(a, n):
    if a == 0:
        pp(a + 1, n)
    elif a == n:
        print('{}'.format(a))
    else:
        print('{}'.format(a), end=' ')
        pp(a + 1, n)


n = int(input())

pp(0, n)
p(n)