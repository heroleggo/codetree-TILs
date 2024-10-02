def insertion(arr):
    result = arr
    for i in range(1, len(arr)):
        j = i - 1
        key = result[i]
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

n = int(input())

data = list(map(int, input().split()))

result = insertion(data)

print(' '.join([str(x) for x in result]))