def bubble(arr):
    result = arr
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

n = int(input())
data = list(map(int, input().split()))

result = bubble(data)

print(' '.join([str(x) for x in result]))