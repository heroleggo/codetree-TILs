[a, b, c] = [int(x) for x in input().split()]

def getMin(*args):
    return min(args)

print(getMin(a, b, c))