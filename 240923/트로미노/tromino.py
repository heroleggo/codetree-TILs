[n, m] = [int(x) for x in input().split()]

board = []

for i in range(0, n):
    board.append([int(x) for x in input().split()])

result = -1

# check pattern 1
for i in range(0, n - 1):
    for j in range(0, n - 1):
        values = [board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]]
        values.sort()
        result = max(result, sum(values) - min(values))


# check pattern 2 - 1
for i in range(0, n - 2):
    for j in range(0, n):
        result = max(result, board[i][j] + board[i + 1][j] + board[i + 2][j])

# check pattern 2 - 2
for i in range(0, n):
    for j in range(0, n - 2):
        result = max(result, board[i][j] + board[i][j + 1] + board[i][j + 2])

print(result)