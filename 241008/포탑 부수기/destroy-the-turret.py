from collections import deque

[n, m, k] = list(map(int, input().split()))

turrets = []

attack_history = []

for i in range(n):
    turrets.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def set_attacker():
    power = 9999
    l = []
    for i in range(n):
        for j in range(m):
            if turrets[i][j] < power and turrets[i][j] != 0:
                power = turrets[i][j]
    for i in range(n):
        for j in range(m):
            if turrets[i][j] == power:
                l.append([i, j])
    for pos in l:
        try:
            pos.append(attack_history.index(pos))
        except ValueError:
            pos.append(-1)
    l.sort(key=lambda x: (-x[2], -(x[0] + x[1]), -x[1]))
    turrets[l[0][0]][l[0][1]] += (n + m)
    return [l[0][0], l[0][1]]

def set_target():
    power = -1
    l = []
    for i in range(n):
        for j in range(m):
            if turrets[i][j] > power and turrets[i][j] != 0:
                power = turrets[i][j]
    for i in range(n):
        for j in range(m):
            if turrets[i][j] == power:
                l.append([i, j])
    for pos in l:
        try:
            pos.append(attack_history.index(pos))
        except ValueError:
            pos.append(-1)
    l.sort(key=lambda x: (x[2], x[0] + x[1], x[1]))
    return [l[0][0], l[0][1]]

def track(arr, target):
    [x, y] = target
    result = [target]
    cnt = 0
    while cnt < 10:
        cnt += 1
        [nx, ny] = arr[x][y]
        x, y = nx, ny
        if arr[nx][ny] != 0:
            result.append([nx, ny])
        else:
            break
    return result


def print_arr(arr):
    result = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > result:
                result = arr[i][j]
    print(result)

def dfs(x, y, visited, parents):
    for i in range(4):
        nx = (x + dx[i]) % n
        ny = (y + dy[i]) % m
        if turrets[nx][ny] != 0:
            if visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                parents[nx][ny] = [x, y]
                dfs(nx, ny, visited, parents)

def get_attack_path(attack, target):
    visited = [[101 for _ in range(m)] for j in range(n)]
    parent = [[0 for _ in range(m)] for j in range(n)]

    visited[attack[0]][attack[1]] = 1

    dfs(attack[0], attack[1], visited, parent)

    if visited[target[0]][target[1]] != 101:
        path = track(parent, target)
        return path
    else:
        return -1

def attack_laser(path, attack_pos):
    [ax, ay] = attack_pos
    for idx, pos in enumerate(path):
        [x, y] = pos
        if idx == 0:
            turrets[x][y] = max(0, turrets[x][y] - turrets[ax][ay])
        else:
            turrets[x][y] = max(0, turrets[x][y] - (turrets[ax][ay] // 2))
    return

def attack_cannon(target_pos, attack_pos):
    attacked = []
    [x, y] = target_pos
    power = turrets[attack_pos[0]][attack_pos[1]]

    cannon_range = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for idx, delta in enumerate(cannon_range):
        nx = (x + delta[0]) % n
        ny = (y + delta[1]) % m
        next_turret = turrets[nx][ny]
        if next_turret != 0:
            if idx == 0:
                turrets[nx][ny] = max(0, turrets[nx][ny] - power)
            else:
                turrets[nx][ny] = max(0, turrets[nx][ny] - (power // 2))
            attacked.append([nx, ny])
    return attacked

def repair_without_param(lst):
    for i in range(n):
        for j in range(m):
            if turrets[i][j] != 0 and [i, j] not in lst:
                turrets[i][j] += 1

def do_turn():
    target_pos = set_target()
    attack_pos = set_attacker()
    path = get_attack_path(attack_pos, target_pos)
    if path == -1:
        # print('cannon')
        attacked = attack_cannon(target_pos, attack_pos)
        repair_without_param(attacked + [attack_pos])
    else:
        # print('laser')
        attack_laser(path, attack_pos)
        repair_without_param(path + [attack_pos])
    attack_history.append(attack_pos)
    return



for i in range(k):
    do_turn()

print_arr(turrets)