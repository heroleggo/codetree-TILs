[m, d] = [int(x) for x in input().split()]

def check(m, d):
    if m == 2:
        if 1 <= d <= 28:
            return "Yes"
        else:
            return "No"
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= d <= 31:
            return "Yes"
        else:
            return "No"
    elif m in [4, 6, 9, 11]:
        if 1 <= d <= 30:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(check(m, d))