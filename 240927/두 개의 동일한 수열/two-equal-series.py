n = int(input())

first = sorted([int(x) for x in input().split()])

second = sorted([int(x) for x in input().split()])

flag = True

for i in range(n):
    if first[i] != second[i]:
        flag = False
        break

print("Yes" if flag else "No")