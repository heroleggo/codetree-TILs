[n1, n2] = [int(x) for x in input().split()]

#arr1 = [int(x) for x in input().split()]
#arr2 = [int(x) for x in input().split()]

arr1 = input()
arr2 = input()

def check(a1, a2):
    return a2 in a1

if n2 > n1:
    print("No")
else:
    if check(arr1, arr2):
        print("Yes")
    else:
        print("No")