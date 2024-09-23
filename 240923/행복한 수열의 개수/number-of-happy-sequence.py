[n, m] = [int(x) for x in input().split()]

board = []

for i in range(0, n):
    board.append([int(x) for x in input().split()])

result = 0

# row
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if j != 0:
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 1
        if cnt == m:
            result += 1
            break

for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if j != 0:
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 1
        if cnt == m:
            result += 1
            break

print(result)