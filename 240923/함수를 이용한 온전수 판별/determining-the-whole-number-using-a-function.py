def check(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

[a, b] = [int(x) for x in input().split()]

result = 0

for i in range(a, b + 1):
    if check(i):
        result += 1

print(result)