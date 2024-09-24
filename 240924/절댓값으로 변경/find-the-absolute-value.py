def absolute(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -arr[i]
    return

n = input()

data = [int(x) for x in input().split()]

absolute(data)

print(' '.join([str(x) for x in data]))