def quick(start, end):
    global data
    if start < end:
        # select pivot (mid)
        pivot = partition(start, end)

        quick(start, pivot - 1)
        quick(pivot + 1, end)

def partition(left, right):
    global data
    pivot = left
    i = left + 1
    j = right
    
    while i <= j:
        while data[i] < data[pivot]:
            i += 1
        while data[j] > data[pivot]:
            j -= 1
        if i <= j:
            # swap
            data[i], data[j] = data[j], data[i]
    data[pivot], data[j] = data[j], data[pivot]
    return j

n = int(input())

data = list(map(int, input().split()))

quick(0, len(data) - 1)

print(' '.join([str(x) for x in data]))