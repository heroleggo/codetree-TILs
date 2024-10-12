# init
[N, M, P, C, D] = list(map(int, input().split()))

board = [[0 for _ in range(N)] for _ in range(N)]

rx, ry = tuple(map(int, input().split()))

MIN_DIST = (N ** 2) * 2

# 1,1 -> 0,0
rx, ry = rx - 1, ry - 1

board[rx][ry] = -1

santa_x = [-1 for _ in range(P + 1)]
santa_y = [-1 for _ in range(P + 1)]
santa_stunned = [0 for _ in range(P + 1)]
santa_score = [0 for _ in range(P + 1)]

for _ in range(P):
    santa_idx, s_input_x, s_input_y = tuple(map(int, input().split()))
    santa_x[santa_idx] = s_input_x - 1
    santa_y[santa_idx] = s_input_y - 1
    board[s_input_x - 1][s_input_y - 1] = santa_idx

def all_out():
    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            return False
    return True

def get_distance(pos1, pos2):
    a, b = pos1
    c, d = pos2
    return (a - c) ** 2 + (b - d) ** 2

def get_rudolf_direction():
    min_distance = MIN_DIST # 좌표간 거리는 최대 (N - 1)^2 * 2가 되는데, 더 큰 거리를 기준으로 하기 위해 선정
    candidate = []
    # find nearest santa by order ()
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if board[i][j] > 0:
                distance = get_distance((rx, ry), (i, j))
                if distance == min_distance:
                    candidate.append((i, j))
                elif distance < min_distance:
                    min_distance = distance
                    candidate = [(i, j)]
    candidate.sort(key=lambda x: (-x[0], -x[1]))
    tx, ty = candidate[0]

    # calculate best direction
    direction8 = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
    best = (0, 0)
    dst = get_distance((rx, ry), (tx, ty))
    for d in direction8:
        nx, ny = rx + d[0], ry + d[1]
        distance = get_distance((nx, ny), (tx, ty))
        if distance < dst:
            dst = distance
            best = d
    return best[0], best[1]

def out_of_board(r, c):
    return r < 0 or r >= N or c < 0 or c >= N

def get_santa_direction(santa_index):
    direction4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    best = (0, 0)
    sx, sy = santa_x[santa_index], santa_y[santa_index]
    min_dist = get_distance((sx, sy), (rx, ry))
    for d in direction4:
        if out_of_board(sx + d[0], sy + d[1]) or board[sx + d[0]][sy + d[1]] > 0:
            continue
        distance = get_distance((sx + d[0], sy + d[1]), (rx, ry))
        if distance < min_dist:
            min_dist = distance
            best = d
    return best

# index의 산타가 부딪힘, 산타의 이동 방향 또는 루돌프의 이동 방향으로, 산타가/루돌프가
def hit(santa_index, direction, by):
    global santa_stunned, board
    # real_direction : 산타의 실제 이동 방향
    # power : 충돌 산타의 이동거리
    # inner_power : 상호작용 산타의 이동거리
    real_direction = (0, 0)
    power = D - 1 if by == 'santa' else C
    score = D if by == 'santa' else C

    # 산타가 이동해서 충돌 -> 산타 이동의 반대방향으로 이동하며 상호작용 탐색 및 이동 (산타는 이동한다. 여기서 상호작용까지 모두 이동)
    if by == 'santa':
        # reverse direction to move santa
        real_direction = (-direction[0], -direction[1])
    # 루돌프가 이동해서 충돌 -> 루돌프 충돌 방향 그대로 이동하며 상호작용 탐색 및 이동 (루돌프는 이동하지 않는다. simulate() 함수 안에서 이동)
    else:
        real_direction = (direction[0], direction[1])

    # 연쇄작용 탐색을 위해 스택 선언
    # 스택에는 이동하는 산타의 인덱스만 들어감. 만약 범위 바깥으로 나간다면 범위 밖의 인덱스가 스택에 기록되지는 않는다.
    stack = []
    stack.append(santa_index)
    while True:
        # 종료조건 : 연쇄작용 끝 산타의 다음 이동방향에 산타가 없거나, 범위 바깥으로 나가는 경우
        top = stack[-1]
        sx, sy = santa_x[top], santa_y[top]
        nx, ny = -1, -1
        if top == santa_index:
            nx, ny = sx + power * real_direction[0], sy + power * real_direction[1]
        else:
            nx, ny = sx + real_direction[0], sy + real_direction[1]
        if out_of_board(nx, ny) or board[nx][ny] == 0:
            break
        # 다음 위치의 산타 번호를 스택에 넣기
        stack.append(board[nx][ny])
    # 산타의 이동 -> 스택을 pop 하며 탈락 처리 또는 이동 처리
    while stack:
        top = stack.pop()
        dx, dy = 0, 0
        sx, sy = santa_x[top], santa_y[top]
        if top == santa_index:
            santa_stunned[top] = 2
            santa_score[top] += score
            dx, dy = power * real_direction[0], power * real_direction[1]
        else:
            dx, dy = real_direction[0], real_direction[1]
        if out_of_board(sx + dx, sy + dy): # 탈락 처리 -> 보드 비우기
            board[sx][sy] = 0
            santa_stunned[top] = -1
        else:
            move(top, (dx, dy), 'santa')
    return

def move(santa_index, direction, move_type):
    global board, santa_x, santa_y, rx, ry
    if move_type == 'rudolf':
        board[rx][ry] = 0
        rx, ry = rx + direction[0], ry + direction[1]
        board[rx][ry] = -1
    else:
        sx, sy = santa_x[santa_index], santa_y[santa_index]
        nx, ny = sx + direction[0], sy + direction[1]
        board[sx][sy] = 0
        santa_x[santa_index], santa_y[santa_index] = nx, ny
        board[nx][ny] = santa_index
    return

# return value -1 : all santas out of board, 0 -> else
def simulate():
    global santa_stunned, santa_score
    if all_out():
        return -1
    # move rudolf
    r_dx, r_dy = get_rudolf_direction()

    # print('[rudolf] current : {} {}, move to {} {}'.format(rx, ry, rx + r_dx, ry + r_dy))
    # if next position is santa -> hit, else just move to next position
    if board[rx + r_dx][ry + r_dy] > 0:
        # print('[hit by rudolf]')
        hit(board[rx + r_dx][ry + r_dy], (r_dx, r_dy), 'rudolf')

    # if hit santa, after santa's move, move rudolf to next position
    move(-1, (r_dx, r_dy), 'rudolf')

    # move santa
    for i in range(1, P + 1):
        # -1 -> out, n with n > 0 -> stunned for n turns
        if santa_stunned[i] != 0:
            continue
        sx, sy = santa_x[i], santa_y[i]
        s_dx, s_dy = get_santa_direction(i)
        # print('[SANTA {}] current : {} {}, move to {} {}'.format(i, sx, sy, sx + s_dx, sy + s_dy))
        if board[sx + s_dx][sy + s_dy] == -1:
            # print('[hit by santa {}]'.format(i))
            hit(i, (s_dx, s_dy), 'santa')
        else: # 여기서는 산타에 의해 산타가 밀려나지 않는다. (안겹치는 방향으로 이동하거나 이동하지 않기 때문)
            move(i, (s_dx, s_dy), 'santa')

    # after turn, live santa get 1 point
    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            santa_score[i] += 1
            if santa_stunned[i] > 0:
                santa_stunned[i] -= 1
    return 0

def print_score():
    print(' '.join(map(str, santa_score[1:])))

def print_arr(arr):
    for a in arr:
        print(a)

for t in range(M):
    # print('[Turn {}]'.format(t + 1))
    res = simulate()
    # print_arr(board)
    # print_score()
    if res == -1:
        break

# print('[after all turn or break]')
print_score()