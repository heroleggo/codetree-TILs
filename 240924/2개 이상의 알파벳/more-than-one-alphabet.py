def check(string):
    for idx in range(len(string)):
        if idx == 0:
            continue
        else:
            if string[idx] != string[idx - 1]:
                return "Yes"
    return "No"

data = input()

print(check(data))