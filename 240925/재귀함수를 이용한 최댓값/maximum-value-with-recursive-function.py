def findMax(arr, n):
    if n == 1:
        return arr[0]
    else:
        maxNum = findMax(arr, n - 1)
        if maxNum > arr[n - 1]:
            return maxNum
        else:
            return arr[n - 1]

n = int(input())
data = [int(x) for x in input().split()]


print(findMax(data, n))