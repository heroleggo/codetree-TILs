def s(start, n):
    if start == n:
        return n
    else:
        return start + s(start + 2, n)

n = int(input())

if n % 2 == 0:
    print(s(2, n))
else:
    print(s(1, n))