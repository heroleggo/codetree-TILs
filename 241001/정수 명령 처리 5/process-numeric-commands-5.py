n = int(input())

data = []

for i in range(n):
    command = input().split()
    if command[0] == 'push_back':
        data.append(command[1])
    elif command[0] == 'pop_back':
        data.pop()
    elif command[0] == 'size':
        print(len(data))
    elif command[0] == 'get':
        print(data[int(command[1]) - 1])