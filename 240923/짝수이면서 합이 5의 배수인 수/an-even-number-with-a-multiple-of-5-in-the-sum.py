def check(data):
    s = sum(int(n) for n in data)
    if int(data) % 2 == 0 and s % 5 == 0:
        return "Yes"
    return "No"

n = input()

print(check(n))