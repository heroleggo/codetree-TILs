import math

n = int(input())

def calc(a):
    data = a * (a + 1) / 2
    return data / 10

print(math.floor(calc(n)))