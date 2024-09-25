def calc(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        n = int(n / 2)
        return calc(n, cnt + 1)
    else:
        n = int(n / 3)
        return calc(n, cnt + 1)

cnt = 0
n = int(input())



print(calc(n, cnt))