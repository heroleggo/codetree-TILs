n = int(input())

data = [int(x) for x in input().split()]

def change(arr):
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)

change(data)

print(' '.join([str(x) for x in data]))