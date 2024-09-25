def calc(arr, n):
    if n == 0:
        return int(arr[n]) ** 2
    else:
        return int(arr[n]) ** 2 + calc(arr, n - 1)

n = input()
print(calc(n, len(n) - 1))