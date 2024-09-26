def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calc(arr, length):
    if length == 0:
        return arr[length]
    return lcm(calc(arr, length - 1), arr[length])

n = int(input())
data = [int(x) for x in input().split()]

print(calc(data, n - 1))