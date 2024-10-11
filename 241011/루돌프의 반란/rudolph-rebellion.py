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

# add santa to list (change 1, 1 base to 0, 0 base), (change list index -> start from 0)
for _ in range(P):
    [idx, x, y] = list(map(int, input().split()))
    santa_x[idx] = x - 1
    santa_y[idx] = y - 1
    board[x - 1][y - 1] = idx

def print_arr(ar):
    for i in range(len(ar)):
        print(ar[i])

def get_distance(start, target):
    [sx, sy] = start
    [tx, ty] = target
    return (tx - sx) ** 2 + (ty - sy) ** 2

def find_santa_index(r, c):
    for i in range(1, P):
        if santa_x[i] == r and santa_y[i] == c:
            return i
    return -1

# 보드 안에서 데이터 움직이기
# pos 의 데이터 direction 방향으로 power만큼 움직이기
# 만약 목적지에 데이터가 존재할 경우, 해당 목적지의 데이터를 먼저 1만큼 옮기기
def move(pos, direction, power):
    global board, santa_stunned, santa_x, santa_y
    # cx = santa_x[pos]
    # cy = santa_y[pos]
    [dx, dy] = direction
    # nx = cx + dx * power
    # ny = cy + dy * power
    # 바로 나가지는 경우 체크
    # if not in_board(nx, ny):
    #     santa_stunned[pos] = -1 # 탈락 처리 후 함수 반환
    #     board[cx][cy] = 0 # 원래 있던 자리 비우기
    #     return

    stack = [pos]

    # 로직 구조
    # 0. 이동 시작 하는 산타 순서 스택에 push
    # 1. 스택 top 측정 -> 첫 놈일 경우 power 만큼, 그렇지 않은 경우 1만큼 이동한 값을 nx, ny로 선언
    # 2. nx, ny가 보드 안에 있으면서, 산타가 없으면 while문 중단
    # 2-2. nx, ny가 보드 바깥이라면 해당 번호의 산타를 탈락 처리하고 현재 위치를 0으로 변경한 후 중단
    # 3. 산타가 nx, ny 위치에 있는 경우 해당 nx, ny에 해당하는 산타 순서 push
    # 4. 계속 반복하다 보면, 빠져나와있음
    while True:
        # print('in searching movement, stack is : ', stack)
        top = stack[len(stack) - 1]
        p = 1
        if top == pos:
            p = power
        cx, cy = santa_x[top], santa_y[top]
        nx, ny = cx + dx * p, cy + dy * p

        if not in_board(nx, ny):
            santa_stunned[top] = -1
            break

        index = find_santa_index(nx, ny)
        if index == -1:
            break
        stack.append(index)

    # print('after searching movement, stack is : ', stack)
    # 실제 수정
    while len(stack) > 0:
        top = stack.pop()
        cx, cy = santa_x[top], santa_y[top]
        if top == pos:
            p = power
        nx, ny = cx + dx * p, cy + dy * p

        if not in_board(nx, ny):
            santa_stunned[top] = -1
            board[cx][cy] = 0
        else:
            board[nx][ny] = board[cx][cy]
            board[cx][cy] = 0
            santa_x[top] = nx
            santa_y[top] = ny

    # index = find_santa_index(nx, ny)
    # while index != -1:
    #     # top
    #     [c, n] = stack[len(stack) - 1]
    #     (tx, ty) = n
    #     stack.append([(tx, ty), (tx + dx, ty + dy)])
    #     if not in_board(tx + dx, ty + dy):
    #
    #     if no_santa(tx + dx, ty + dy):
    #         break
    #     else:
    #
    #     if not no_santa
    # if not no_santa(nx, ny):
    #     stack.append([cx, cy])
    #     index = find_santa_index(nx, ny)
    #     while index != -1:
    #         sx, sy = santa_x[index], santa_y[index]
    #
    #         stack.append([sx, sy])
    #     # 연쇄이동 수행
    #     move(index, direction, 1)
    # # 산타도 없고, 외부도 아닌 경우
    # board[nx][ny] = board[cx][cy]
    # board[cx][cy] = 0
    # santa_x[pos] = nx
    # santa_y[pos] = ny
    return

# position : 맞은 산타의 번호, direction : 방향, by : 산타 또는 루돌프
# 점수 증감 발생
# 이후 연쇄 이동 호출
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
        # 충돌 전 루돌프와의 거리 1, 루돌프 -> 산타 방향, 즉 산타 이동 반대방향으로 이미 1칸 이동한 것 과 같음
        move(position, [dx, dy], D - 1)
    return

def in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def no_santa(r, c):
    return board[r][c] <= 0

def all_out():
    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            return False
    return True

def simulate():
    global r_pos, santa_stunned, santa_score
    # get nearest distance (우하단 부터 탐색해 루돌프 우선순위에 맞춘다.)
    if all_out():
        return -1
    [rx, ry] = r_pos
    curr = [-1, -1]
    short_distance = 3000 # ((50 ** 2) * 2) 보다 큰 값
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if board[i][j] > 0:
                distance = get_distance(r_pos, [i, j])
                if distance < short_distance:
                    short_distance = distance
                    curr = [i, j]
    # move rudolf -> calculate next direction
    dx, dy = 0, 0
    if curr[0] < rx:
        dx = -1
    elif curr[0] > rx:
        dx = 1
    if curr[1] < ry:
        dy = -1
    elif curr[1] > ry:
        dy = 1
    nx, ny = rx + dx, ry + dy

    # if crash by rudolf
    if nx == curr[0] and ny == curr[1]:
        index = find_santa_index(nx, ny)
        hit(index, [dx, dy], 'rudolf')

    # after every move of santa caused by rudolf, move rudolf to direction
    r_pos = [nx, ny]
    board[nx][ny] = -1
    # after move, previous is empty
    board[rx][ry] = 0

    # print('[santa move start]')
    for i in range(1, P + 1):
        # 기절 or 탈락 -> 못움직임
        if santa_stunned[i] != 0:
            continue
        # 최단거리 탐색
        sx, sy = santa_x[i], santa_y[i]
        current_distance = get_distance([sx, sy], r_pos)
        selected = -1
        # for j in range(4):
        #     nx, ny = sx + dx4[j], sy + dy4[j]
        #     if in_board(nx, ny) and no_santa(nx, ny):
        #         if nx == r_pos[0] and ny == r_pos[1]:
        #             print('santa {} found rudolf, lets hit!'.format(i))
        #             hit(i, [dx4[j], dy4[j]], 'santa')
        #             break
        #         else:
        #             print('santa {} not found rudolf'.format(i))
        #         distance = get_distance([nx, ny], r_pos)
        #         if distance < current_distance:
        #             move(i, [dx4[j], dy4[j]], 1)
        #             break
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
                # print('[santa {} hit rudolf]'.format(i))
                hit(i, [dx4[selected], dy4[selected]], 'santa')
            else:
                move(i, [dx4[selected], dy4[selected]], 1)

    # print('[santa move finished]')
    for i in range(1, P + 1):
        if santa_stunned[i] != -1:
            santa_score[i] += 1
        if santa_stunned[i] > 0:
            santa_stunned[i] -= 1
    # print('score : ', santa_score)
    # print('stunned : ', santa_stunned)
    return 0

def print_score():
    result = []
    for i in range(1, P + 1):
        result.append(str(santa_score[i]))
    print(' '.join(result))

for t in range(M):
    # print('------turn : {}------'.format(t + 1))
    res = simulate()
    # print_arr(board)
    if res == -1:
        break

print_score()