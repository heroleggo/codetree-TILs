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
    for i in range(max(0, r - size - 1), min(len(data), r + size)):
        for j in range(max(0, c - size - 1), min(len(data), c + size)):
            diff = abs(r - i) + abs(c - j)
            if data[i][j] == 1 and diff <= size:
                result += 1
    return result


def func(data, size, value):
    maxValue = getValue(data, value)
    result = -1
    for i in range(len(data)):
        for j in range(len(data)):
            size = 0
            while True:
                cost = getCost(size)
                if cost > maxValue:
                    break
                else:
                    calculatedCount = calc(data, i, j, size)
                    if calculatedCount * value > cost:
                        result = max(calculatedCount, result)
                    size += 1
    return result


[n, m] = [int(x) for x in input().split()]

board = []

for i in range(n):
    board.append([int(x) for x in input().split()])

print(func(board, n, m))