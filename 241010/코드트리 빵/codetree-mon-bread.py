from collections import deque

[n, m] = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]

# index 0 base
store = [[i - 1 for i in list(map(int, input().split()))] for _ in range(m)]

basecamp = []

# time
t = 0

# dx, dy
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# init basecamp
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            basecamp.append((i, j))

# 최초 실행 시 사용, 각 편의점 별 베이스캠프 선매칭
# 결과 -> 각 인덱스 i별 i + 1분에 배치될 최초의 위치가 된다.
def match_store_and_basecamp():
    camp_copy = [x for x in basecamp]
    result = []
    for s in store:
        tmp = (20, 20) # 최대 15, 15, 최초 선언시에만 20, 20 사용
        sx, sy = s
        min_distance = 100000 # 절대 불가능한 숫자 사용
        for c in camp_copy:
            cx, cy = c
            diff = abs(sx - cx) + abs(sy - cy)
            if diff == min_distance:
                tx, ty = tmp
                if tx == cx:
                    if ty > cy:
                        tmp = (cx, cy)
                elif tx > cx:
                    tmp = (cx, cy)
            elif diff < min_distance:
                min_distance = diff
                tmp = (cx, cy)
        result.append(tmp)
    return result

initial_apply_position = match_store_and_basecamp()

humans = []

def apply(idx):
    x, y = initial_apply_position[idx]
    humans.append([x, y, False])
    return

def all_clear():
    for human in humans:
        x, y, is_arrived = human
        if not is_arrived:
            return False
    return True

def check_position(x, y):
    return 0 <= x < n and 0 <= y < n

# human : 움직이는 사람
# idx : 몇 번째 편의점
def move(human, idx):
    [tx, ty] = store[idx]
    x, y, is_arrived = human
    visited = [[0 for _ in range(n)] for __ in range(n)]
    parent = [[0 for _ in range(n)] for __ in range(n)]
    queue = deque()
    queue.append([x, y])
    while queue:
        [cx, cy] = queue.popleft()
        if cx == tx and cy == ty:
            break
            # return [cx, cy] # 편의점 방문처리를 위해 반환
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if check_position(nx, ny) and board[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    parent[nx][ny] = [cx, cy]
                    queue.append([nx, ny])
                elif visited[cx][cy] + 1 < visited[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    parent[nx][ny] = [cx, cy]
                    queue.append([nx, ny])
    print_arr(parent)
    human = (parent[x][y][0], parent[x][y][1], is_arrived)
    return human

def check(data):
    for i in data:
        [x, y] = i
        board[x][y] = 1
    return

def print_arr(ar):
    for i in range(len(ar)):
        print(ar[i])

def compare(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

cnt = 0

while True and cnt < 10:
    print(t)
    # step 1. 배치된 사용자에 대해 움직이기
    finished = []
    for idx, h in enumerate(humans):
        (x, y, is_arrived) = move(h, idx)
        if compare(store[idx], [x, y]):
            finished.append([x, y])
    # step 2. 편의점 도착 확인 및 처리
    print(finished)
    if finished:
        check(finished)
    # step 3. 미배치 인원이 있는 경우 배치
    if t < m:
        apply(t)
    if all_clear():
        break
    t += 1
    cnt += 1

print(t)