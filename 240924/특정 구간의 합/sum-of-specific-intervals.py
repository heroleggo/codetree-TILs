[n, m] = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

params = []

for i in range(m):
    params.append([int(x) for x in input().split()])

def calc(param):
    global arr
    result = 0
    for i in range(param[0] - 1, param[1]):
        result += arr[i]
    return result

for param in params:
    print(calc(param))