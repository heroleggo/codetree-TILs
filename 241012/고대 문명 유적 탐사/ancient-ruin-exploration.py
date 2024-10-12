from collections import deque

[K, M] = list(map(int, input().split()))

# init board
board = [list(map(int, input().split())) for _ in range(5)]

# init wall
wall = list(map(int, input().split()))

ptr = 0

result = []

def copy_array():
    cp = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(board[i][j])
        cp.append(tmp)
    return cp

def simulate():
    global ptr, board
    # print_arr(board)
    # print('current pointer : {}'.format(ptr))
    # 각 좌상단에서 회전 결과 별 최고 밸류를 저장할 곳
    max_board = []

    max_value = 0 # 보드의 모든 데이터가 3개 이상씩 묶여서 합이 25가 될 경우 보다 큰 숫자
    # pos = (-1, -1)
    # deg = 0

    for k in [90, 180, 270]:
        for j in range(3):
            for i in range(3):
                # 유적 복사
                board_copy = copy_array()
                rotated_data = rotate((i, j), k)
                # apply rotated data to copy-board
                for a in range(3):
                    for b in range(3):
                        board_copy[i + a][j + b] = rotated_data[a][b]
                # 얻을 수 있는 가치 합 계산 및 데이터 갱신
                val, processed_board = bfs(board_copy)
                if val > max_value:
                    max_value = val
                    max_board = processed_board
                    # pos = (i, j)
                    # deg = k
    if max_value == 0:
        max_board = copy_array()
    # print('[Searching finished]')
    # print(pos, deg)
    # print_arr(max_board)
    # 여기까지 하면 모든 데이터가 갱신되어 최고 우선순위의 결과를 만들어 내는 보드 상태가 max_board에 들어감
    # 이후 삭제 처리 -> 데이터 삽입 -> 삭제처리 연쇄 수행하며 결과값 증가시킴
    # 로직 -> max_board에서 데이터를 조정하는 BFS 수행하면서(함수X) 보드 내 검사값이 0이 될때까지 반복
    # print('[Chaining started]')
    bfs_result = 0
    while True:
        # print_arr(max_board)
        for i in range(5):
            for j in range(5):
                if max_board[4 - j][i] == 0:
                    max_board[4 - j][i] = wall[ptr]
                    ptr += 1
        # print_arr(max_board)
        bfs_result, max_board = bfs(max_board)
        if bfs_result == 0:
            break
        else:
            max_value += bfs_result
    # 턴 종료 시점에 실제 보드에 변경된 데이터 반영
    # print('[Chaining finished]')
    for i in range(5):
        for j in range(5):
            board[i][j] = max_board[i][j]
    if max_value == 0:
        return -1
    result.append(max_value)
    return 0

def in_board(r, c):
    return 0 <= r < 5 and 0 <= c < 5

# 데이터에 대해 각 위치 별 BFS 통해서 크기 추출 및 3개 이상의 경우 데이터 더해서 sum 반환
def bfs(data):
    bfs_res = 0
    visited = [[0 for _ in range(5)] for _ in range(5)]
    queue = deque()
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1 or data[i][j] == 0:
                continue
            queue.append((i, j))
            cnt = 0
            curr = data[i][j]
            chained = set()
            while queue:
                (x, y) = queue.popleft()
                delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d in delta:
                    nx, ny = x + d[0], y + d[1]
                    if in_board(nx, ny) and data[nx][ny] == curr and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        chained.add((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
            if cnt >= 3:
                bfs_res += cnt
                # print('data set : {}'.format(chained))
                for pos in chained:
                    data[pos[0]][pos[1]] = 0
    return bfs_res, data

# 좌상단 튜플 lu 기준 deg 만큼 회전한 새로운 3 X 3 격자 반환
def rotate(lu, deg):
    x, y = lu
    # 3 X 3
    rotate_result = [[0 for _ in range(3)] for _ in range(3)]
    if deg == 90:
        for i in range(3):
            for j in range(3):
                rotate_result[j][2 - i] = board[x + i][y + j]
    elif deg == 180:
        for i in range(3):
            for j in range(3):
                rotate_result[2 - i][2 - j] = board[x + i][y + j]
    else:
        for i in range(3):
            for j in range(3):
                rotate_result[2 - j][i] = board[x + i][y + j]
    return rotate_result

def print_arr(arr):
    for a in arr:
        print(a)

# simulate()
# 실제 실행부
for _ in range(K):
    res = simulate()
    if res == -1:
        break

print(' '.join(map(str, result)))