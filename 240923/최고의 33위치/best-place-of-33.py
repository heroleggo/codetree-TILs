n = int(input())

board = []

def calc(data, x, y):
    result = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            result += data[i][j]
    return result

for i in range(0, n):
    board.append([int(x) for x in input().split()])

result = -1

for i in range(0, n - 2):
    for j in range(0, n - 2):
        tempValue = calc(board, i, j)
        result = max(result, tempValue)

print(result)