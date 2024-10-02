def getDigit(num, pos):
    data = str(num).zfill(6)
    return int(data[pos - 1])

def radix(arr):
    result = arr
    for pos in range(6, 0, -1):
        data = [[] for x in range(10)]
        for d in result:
            digit = getDigit(d, pos)
            data[digit].append(d)
        
        new_result = []
        for i in range(10):
            for j in range(len(data[i])):
                new_result.append(data[i][j])
        
        result = new_result
    return result

n = int(input())
data = list(map(int, input().split()))

result = radix(data)

print(' '.join(list(map(str, result))))