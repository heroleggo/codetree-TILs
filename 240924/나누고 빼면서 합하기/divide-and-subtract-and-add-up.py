[n, m] = [int(x) for x in input().split()]
data = [int(x) for x in input().split()]

result = 0

def calc(m):
    global result
    idx = m
    while idx != 1:
        result += data[idx - 1]
        if idx % 2 == 0:
            idx //= 2
        else:
            idx -= 1
    # add first index
    result += data[idx - 1]

calc(m)

print(result)