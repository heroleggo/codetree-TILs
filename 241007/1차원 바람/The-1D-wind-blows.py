[n, m, q] = list(map(int, input().split()))

data = []

commands = []

# wind R -> shift left
def shift_left(row):
    tmp = data[row][0]
    for i in range(m - 1):
        data[row][i] = data[row][i + 1]
    data[row][m - 1] = tmp

# wind L -> shift right
def shift_right(row):
    tmp = data[row][m - 1]
    for i in range(m - 1, 0, -1):
        data[row][i] = data[row][i - 1]
    data[row][0] = tmp

def check(row1, row2):
    for i in range(m):
        if data[row1][i] == data[row2][i]:
            return True
    return False

def do_wind(row, wind_direction, spread):
    if wind_direction == 'L':
        shift_right(row)
    else:
        shift_left(row)
    
    next_direction = 'L' if wind_direction == 'R' else 'R'
    if spread in ['B', 'U'] and row - 1 >= 0 and check(row, row - 1):
        do_wind(row - 1, next_direction, 'U')
    if spread in ['B', 'D'] and row + 1 < n and check(row, row + 1):
        do_wind(row + 1, next_direction, 'D')

    return


for i in range(n):
    data.append(input().split())

for i in range(q):
    [row, direction] = input().split()
    commands.append([int(row) - 1, direction])

for command in commands:
    do_wind(command[0], command[1], 'B')

for i in range(n):
    print(' '.join(data[i]))