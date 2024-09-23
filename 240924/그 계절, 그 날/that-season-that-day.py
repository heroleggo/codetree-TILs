def checkYoon(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def checkDate(y, m, d):
    if m == 2:
        if checkYoon(y):
            if 1 <= d <= 29:
                return True
            else:
                return False
        else:
            if 1 <= d <= 28:
                return True
            else:
                return False
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= d <= 31:
            return True
        else:
            return False
    elif m in [4, 6, 9, 11]:
        if 1 <= d <= 30:
            return True
        else:
            return False

[y, m, d] = [int(x) for x in input().split()]

def toSeason(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"

if checkDate(y, m, d):
    print(toSeason(m))
else:
    print(-1)