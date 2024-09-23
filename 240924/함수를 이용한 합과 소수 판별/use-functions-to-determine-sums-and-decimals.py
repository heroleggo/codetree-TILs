import math

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def checkSum(n):
    s = sum([int(x) for x in str(n)])
    return s % 2 == 0

[a, b] = [int(x) for x in input().split()]

result = 0

for i in range(a, b + 1):
    if isPrime(i) and checkSum(i):
        result += 1

print(result)