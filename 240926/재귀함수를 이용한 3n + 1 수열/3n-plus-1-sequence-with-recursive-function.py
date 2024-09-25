def calc(cnt, n):
    if n == 1:
        return cnt
    else:
        if n % 2 == 0:
            return calc(cnt + 1, n // 2)
        else:
            return calc(cnt + 1, n * 3 + 1)

n = int(input())

print(calc(0, n))