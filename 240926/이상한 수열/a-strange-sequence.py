import math

def calc(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return calc(math.floor(n / 3)) + calc(n - 1)

n = int(input())
print(calc(n))