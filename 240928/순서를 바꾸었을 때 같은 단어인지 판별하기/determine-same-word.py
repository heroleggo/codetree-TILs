a = input()
b = input()

if len(a) != len(b):
    print("No")
else:
    sa = sorted(a)
    sb = sorted(b)
    if ''.join(sa) != ''.join(sb):
        print("No")
    else:
        print("Yes")