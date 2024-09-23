def checkYear(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return "false"
        return 'true'
    return 'false'

n = int(input())

print(checkYear(n))