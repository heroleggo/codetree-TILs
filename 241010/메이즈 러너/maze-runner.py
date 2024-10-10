[n, m, k] = list(map(int, input().split()))

class Human:
    def __init__(self, pos):
        self.pos = [pos[0] - 1, pos[1] - 1] # r, c -> 0,0으로 조정하기 위해 1씩 감소
        self.is_exit = False

maze = []

human = []

move_count = 0

# set maze
for i in range(n):
    maze.append(list(map(int, input().split())))


for i in range(m):
    human.append(Human(list(map(int, input().split()))))

original_exit = list(map(int, input().split()))

# 좌표를 0, 0 기준으로 변경
maze_exit = [original_exit[0] - 1, original_exit[1] - 1]

# 모두 탈출했는지 체크하는 함수
def check_all_clear():
    for h in human:
        if not h.is_exit:
            return False
    return True

# 해당 좌표가 미로 내 존재하는지 확인
def check_pos(curr):
    x, y = curr
    return 0 <= x < n and 0 <= y < n

# 거리 측정 함수 (실제 거리) (정사각형 구성 시 사용, curr은 무조건 좌상단)
def get_real_distance(curr, target):
    [a, b] = curr
    [c, d] = target
    return (c - a) ** 2 + (d - b) ** 2

# 거리 측정 함수 (주어진 조건)
def get_distance(curr, target):
    [a, b] = curr
    [c, d] = target
    return abs(a - c) + abs(b - d)

# 전체 사용자 대상으로 움직이기
# 만약 움직인 경로가 출구일 경우, 사용자 탈출 처리
def move():
    global move_count
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for h in human:
        if h.is_exit:
            continue
        [x, y] = h.pos
        current_distance = get_distance(h.pos, maze_exit)
        next_pos_candidate = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            next_distance = get_distance([nx, ny], maze_exit)
            if check_pos((nx, ny)) and maze[nx][ny] == 0 and next_distance < current_distance:
                next_pos_candidate.append([nx, ny])
        if len(next_pos_candidate) != 0:
            if maze_exit == next_pos_candidate[0]:
                h.is_exit = True
            move_count += 1
            h.pos = next_pos_candidate[0]
    return

# 0, 0부터 한 변의 크기가 size인 정사각형을 만들어 x, y의 좌표를 차례로 증가시키며 출구/사람 존재하는지 탐색
def check_exit_and_human(size):
    for x in range(n - size):
        for y in range(n - size):
            if maze_exit[0] < x or maze_exit[1] < y:
                continue
            if maze_exit[0] - x > size - 1 or maze_exit[1] - y > size - 1:#2 * (size - 1):
                continue
            for h in human:
                if h.pos[0] < x or h.pos[1] < y:
                    continue
                if h.pos[0] - x <= size - 1 and h.pos[1] - y <= size - 1 and not h.is_exit:#2 * (size - 1):
                    # found a min-square
                    return [x, y]
    return -1

# 최소 정사각형 탐색, 회전, 내구도 감소
# 좌상단, 우하단 반환
def modify_maze():
    global maze_exit
    global maze
    for s in range(2, n):
        res = check_exit_and_human(s)
        if res != -1:
            [x, y] = res
            tmp = []
            # add original to tmp, do rotate and decrease
            for i in range(s):
                ar = []
                for j in range(s):
                    ar.append(maze[x + i][y + j])
                    # ar.append(maze[x + s - 1 - j][y + i])
                tmp.append(ar)
            # tmp -> 정사각형 값을 회전될 위치에 지정
            for i in range(s):
                for j in range(s):
                    val = tmp[i][j]
                    # val = tmp[j][s - 1 - i]
                    # 값 변경
                    if val > 0:
                        maze[x + j][y + s - 1 - i] = val - 1
                    else:
                        maze[x + j][y + s - 1 - i] = val
            # maze_exit 위치 변경
            maze_exit = [x + (maze_exit[1] - y), y + s - 1 - (maze_exit[0] - x)]
            # human 위치 변경
            for h in human:
                if x <= h.pos[0] < x + s and y <= h.pos[1] < y + s:
                    h.pos = [x + (h.pos[1] - y), y + s - 1 - (h.pos[0] - x)]
            break
    return

# 턴 별로 주어진 로직을 수행하는 함수
def do_logic():
    # step 0. 모든 참가자 탈출 완료 시 -1 반환
    if check_all_clear():
        return -1
    # step 1. 참가자 별 이동 가능 여부 확인 및 여부에 따른 이동 진행
    move()
    # print('before_rotate')
    # print_arr(maze)
    # print_human()
    # print('exit : {} {}'.format(maze_exit[0], maze_exit[1]))
    # step 2. 최소 정사각형 탐색, 미로 회전 및 내구도 감소
    modify_maze()
    return 0

# 결과 출력함수
def print_result():
    print(move_count)
    print('{} {}'.format(maze_exit[0] + 1, maze_exit[1] + 1))
    return

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])

def print_human():
    for h in human:
        print('{} {}, exited : {}'.format(h.pos[0], h.pos[1], h.is_exit))

def func(turn):
    for t in range(turn):
        # print('turn {}'.format(t + 1))
        res = do_logic()
        if res == -1:
            print_result()
            return
        # print('move count : {}'.format(move_count))
        # print_arr(maze)
        # print_human()
        # print('exit : {} {}'.format(maze_exit[0], maze_exit[1]))
        # print()
    print_result()

# print('default')
# print('move count : {}'.format(move_count))
# print_arr(maze)
# print_human()
# print('exit : {} {}'.format(maze_exit[0], maze_exit[1]))
# print()
# 실행
func(k)