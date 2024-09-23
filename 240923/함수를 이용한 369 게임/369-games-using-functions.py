[a, b] = [int(x) for x in input().split()]

def has369(n):
    arr = [int(i) for i in n]
    return 3 in arr or 6 in arr or 9 in arr

def check(n):
    return n % 3 == 0 or has369(str(n))

cnt = 0

for i in range(a, b + 1):
    if check(i):
        cnt += 1

print(cnt)