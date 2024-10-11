from collections import deque

[L, N, Q] = list(map(int, input().split()))

# init chess board
board = [list(map(int, input().split())) for _ in range(L)]

# init knights, 1,1 -> 0,0
knights = []
for _ in range(N):
    [r, c, h, w, k] = list(map(int, input().split()))
    knights.append([r - 1, c - 1, h, w, k])

# init commands, i th order -> i - 1 th index
commands = []
for _ in range(Q):
    [index, d] = list(map(int, input().split()))
    commands.append([index - 1, d])

# dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

hp_list = list([t[4] for t in knights])

# sum of damages among knights
answer = 0

# 직사각형 안에 존재하는 함정 갯수 탐색
# 직사각형이 무조건 체스판 안에 있으므로, 별도의 예외처리 필요 X
def calculate_trap(pos, h, w):
    res = 0
    [x, y] = pos
    for i in range(h):
        for j in range(w):
            if board[x + i][y + j] == 1:
                res += 1
    return res

# 두 직사각형이 겹치는 지 탐색, 각 좌상단 좌표는 좌표 위치가 작은 것 부터 주어짐
# 만약 체력이 0이면 없는 것 취급
# 이동하는 것이 왼쪽, 비교 대상이 오른쪽
def is_intersect(index1, index2, direction):
    [x1, y1, h1, w1, _] = knights[index1]
    [x2, y2, h2, w2, p2] = knights[index2]

    x1_min, x1_max = x1 + dx[direction], x1 + dx[direction] + h1 - 1
    x2_min, x2_max = x2, x2 + h2 - 1
    y1_min, y1_max = y1 + dy[direction], y1 + dy[direction] + w1 - 1
    y2_min, y2_max = y2, y2 + w2 - 1

    if p2 == 0:
        return False

    if x1_max < x2_min or x2_max < x1_min:
        return False
    if y1_max < y2_min or y2_max < y1_min:
        return False
    return True

# 벽만 체크
def can_move(knight, direction):
    [x, y, height, width, _] = knight
    # direction 0, 2 -> 상하
    # direction 1, 3 -> 좌우
    if direction == 0:
        if x - 1 < 0:
            return False
        for i in range(width):
            if board[x - 1][y + i] == 2:
                return False
    elif direction == 1:
        if y + width >= L:
            return False
        for i in range(height):
            if board[x + i][y + width] == 2:
                return False
    elif direction == 2:
        if x + height >= L:
            return False
        for i in range(width):
            if board[x + height][y + i] == 2:
                return False
    else:
        if y - 1 < 0:
            return False
        for i in range(height):
            if board[x + i][y - 1] == 2:
                return False
    return True


def do_command(command):
    global answer, knights
    [idx, direction] = command
    knight = knights[idx]
    # 각 직사각형 탐색
    parents = [[] for _ in range(N)]
    visited = [0 for _ in range(N)]
    candidate = set()
    queue = deque()
    blocked = []
    if can_move(knight, direction):
        candidate.add(idx)
        queue.append(idx)
        visited[idx] = 1
    while queue:
        curr_idx = queue.popleft()
        for i, v in enumerate(knights):
            if i == curr_idx or visited[i] == 1 or v[4] == 0:
                continue
            if is_intersect(curr_idx, i, direction):
                parents[i].append(curr_idx)
                visited[i] = 1
                if can_move(v, direction):
                    candidate.add(i)
                    queue.append(i)
                else:
                    blocked.append(i)
    removal = set()
    for index, p in enumerate(parents):
        if index in blocked:
            for item in p:
                removal.add(item)
    for item in list(removal):
        candidate.discard(item)
    # 찾은 직사각형 이동 및 체력 조정
    for candidate_index in list(candidate):
        [x, y, height, width, hp] = knights[candidate_index]
        # 최초 명령받지 않은 경우, 함정 찾아서 체력 감소
        delta = 0
        if candidate_index != idx:
            trap_cnt = calculate_trap([x + dx[direction], y + dy[direction]], height, width)
            delta = trap_cnt
            if trap_cnt > hp:
                delta = hp
        knights[candidate_index] = [x + dx[direction], y + dy[direction], height, width, hp - delta]
    return

def calc_answer():
    res = 0
    for i, knight in enumerate(knights):
        if knight[4] != 0:
            res += hp_list[i] - knight[4]
    return res

for ind, command in enumerate(commands):
    do_command(command)

print(calc_answer())