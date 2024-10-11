[N, M, P, C, D] = list(map(int, input().split()))

# init board
# rudolf -> -1
# empty -> 0
# santa -> santa's index
board = [[0 for _ in range(N)] for _ in range(N)]

# enter rudolf's position (change 1, 1 base to 0, 0 base)
r_pos = [d - 1 for d in list(map(int, input().split()))]

# rudolf -> -1
board[r_pos[0]][r_pos[1]] = -1

santa_x = [-1 for _ in range(P + 1)]
santa_y = [-1 for _ in range(P + 1)]
santa_score = [0 for _ in range(P + 1)]
santa_stunned = [0 for _ in range(P + 1)]

# for santa
dx4 = [-1, 0, 1, 0]
dy4 = [0, 1, 0, -1]

# add santa to list
for _ in range(P):
    [idx, x, y] = list(map(int, input().split()))
    santa_x[idx] = x - 1
    santa_y[idx] = y - 1
    board[x - 1][y - 1] = idx

def in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def find_santa_index(r, c):
    for i in range(1, P + 1):
        if santa_x[i] == r and santa_y[i] == c and santa_stunned[i] != -1:
            return i
    return -1

def get_distance(start, target):
    [sx, sy] = start
    [tx, ty] = target
    return (tx - sx) ** 2 + (ty - sy) ** 2

def move(pos, direction, power):
    global board, santa_stunned, santa_x, santa_y
    [dx, dy] = direction
    stack = [pos]
    visited = set()

    while True:
        top = stack[-1]
        if top in visited:
            break
        visited.add(top)
        p = power if top == pos else 1
        cx, cy = santa_x[top], santa_y[top]
        nx, ny = cx + dx * p, cy + dy * p

        if not in_board(nx, ny):
            santa_stunned[top] = -1
            santa_x[top] = -1  # 위치 정보 초기화
            santa_y[top] = -1  # 위치 정보 초기화
            break

        index = find_santa_index(nx, ny)
        if index == -1:
            break
        stack.append(index)

    while len(stack) > 0:
        top = stack.pop()
        p = power if top == pos else 1
        cx, cy = santa_x[top], santa_y[top]
        nx, ny = cx + dx * p, cy + dy * p

        board[cx][cy] = 0  # 현재 위치 비우기

        if not in_board(nx, ny):
            santa_stunned[top] = -1
            santa_x[top] = -1  # 위치 정보 초기화
            santa_y[top] = -1  # 위치 정보 초기화
        else:
            board[nx][ny] = top
            santa_x[top] = nx
            santa_y[top] = ny
    return

def hit(position, direction, by):
    global santa_score, santa_stunned
    if by == 'rudolf':
        santa_score[position] += C
        santa_stunned[position] = 2
        move(position, direction, C)
    elif by == 'santa':
        santa_score[position] += D
        santa_stunned[position] = 2
        [dx, dy] = direction
        dx, dy = -dx, -dy
        move(position, [dx, dy], D - 1)
    return

def all_out():
    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            return False
    return True

def no_santa(r, c):
    return board[r][c] <= 0

def simulate():
    global r_pos, santa_stunned, santa_score
    if all_out():
        return -1
    [rx, ry] = r_pos
    curr = [-1, -1]
    short_distance = 3000
    candidates = []
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if board[i][j] > 0:
                distance = get_distance(r_pos, [i, j])
                if distance < short_distance:
                    short_distance = distance
                    candidates = [[i, j]]
                elif distance == short_distance:
                    candidates.append([i, j])

    # 우선순위에 따라 대상 산타 선택
    candidates.sort(key=lambda x: (-x[0], -x[1]))
    curr = candidates[0]
 # 루돌프의 이동 방향 선택
    dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]
    min_distance = get_distance(r_pos, curr)
    best_dx, best_dy = 0, 0
    for i in range(8):
        nx, ny = rx + dx8[i], ry + dy8[i]
        if in_board(nx, ny):
            distance = get_distance([nx, ny], curr)
            if distance < min_distance:
                min_distance = distance
                best_dx, best_dy = dx8[i], dy8[i]

    nx, ny = rx + best_dx, ry + best_dy

    if nx == curr[0] and ny == curr[1]:
        index = find_santa_index(nx, ny)
        hit(index, [best_dx, best_dy], 'rudolf')

    r_pos = [nx, ny]
    board[nx][ny] = -1
    board[rx][ry] = 0

    for i in range(1, P + 1):
        if santa_stunned[i] != 0:
            continue
        sx, sy = santa_x[i], santa_y[i]
        current_distance = get_distance([sx, sy], r_pos)
        selected = -1
        for j in range(4):
            nx, ny = sx + dx4[j], sy + dy4[j]
            if in_board(nx, ny) and no_santa(nx, ny):
                distance = get_distance([nx, ny], r_pos)
                if distance < current_distance:
                    current_distance = distance
                    selected = j
        if selected == -1:
            continue
        else:
            if current_distance == 0:
                hit(i, [dx4[selected], dy4[selected]], 'santa')
            else:
                move(i, [dx4[selected], dy4[selected]], 1)

    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            santa_score[i] += 1
        if santa_stunned[i] > 0:
            santa_stunned[i] -= 1
    return 0

def print_score():
    result = []
    for i in range(1, P + 1):
        result.append(str(santa_score[i]))
    print(' '.join(result))

for t in range(M):
    res = simulate()
    if res == -1:
        break

print_score()