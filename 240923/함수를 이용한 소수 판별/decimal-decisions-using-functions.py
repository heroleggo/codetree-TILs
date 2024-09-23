import math

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

[a, b] = [int(x) for x in input().split()]

result = 0

for i in range(a, b + 1):
    if isPrime(i):
        result += i

print(result)