def getValue(data, value):
    result = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 1:
                result += value
    return result

def getCost(size):
    return size ** 2 + (size + 1) ** 2

def calc(data, r, c, size):
    result = 0
    if size == 0:
        return 1 if data[r - 1][c - 1] == 1 else 0
    for i in range(max(0, (r - 1) - size), min(len(data), r + size)):
        for j in range(max(0, (c - 1) - size), min(len(data), c + size)):
            diff = abs(r - i - 1) + abs(c - j - 1)
            if data[i][j] == 1 and diff <= size:
                result += 1
    return result


def func(data, size, value):
    maxValue = getValue(data, value)
    result = 0
    for i in range(1, len(data) + 1):
        for j in range(1, len(data) + 1):
            size = 0
            while True:
                cost = getCost(size)
                if cost > maxValue:
                    break
                else:
                    calculatedCount = calc(data, i, j, size)
                    if calculatedCount * value >= cost:
                        result = max(calculatedCount, result)
                    size += 1
    return result


[n, m] = [int(x) for x in input().split()]

board = []

for i in range(n):
    board.append([int(x) for x in input().split()])

print(func(board, n, m))