n = int(input())


data = []

for i in range(n):
    data.append(list(map(int, input().split())))

positions = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            positions.append([i, j])

result = -1

def func(k):
    menu = [1, 2, 3]
    selected = []

    def generate(s):
        global result
        if len(s) == k:
            result = max(calc(s), result)
            return
        for i in menu:
            s.append(i)
            generate(s)
            s.pop()
    
    generate(selected)

def calc(selected):
    copy = [[0 for i in range(n)] for j in range(n)]
    for idx, position in enumerate(positions):
        [x, y] = position
        if selected[idx] == 1:
            for i in range(max(0, x - 2), min(n, x + 3)):
                copy[i][y] = 1
        elif selected[idx] == 2:
            for i in range(max(0, x - 1), min(n, x + 2)):
                copy[i][y] = 1
            for i in range(max(0, y - 1), min(n, y + 2)):
                copy[x][i] = 1
        elif selected[idx] == 3:
            copy[x][y] = 1
            for i in range(max(0, x - 1), min(n, x + 2)):
                for j in range(max(0, y - 1), min(n, y + 2)):
                    if abs(x - i) + abs(y - j) == 2:
                        copy[i][j] = 1
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += copy[i][j]
    return ret

func(len(positions))

print(result)