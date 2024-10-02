def selection(arr):
    result = arr
    for i in range(len(result)):
        m = i
        for j in range(m, len(result)):
            if result[j] < result[m]:
                m = j
        result[m], result[i] = result[i], result[m]
    return result

n = int(input())

data = list(map(int, input().split()))

result = selection(data)

print(' '.join([str(x) for x in result]))