a, o, c = input().split()

def add(a, c):
    return str(a) + " + " + str(c) + " = " + str(int(a) + int(c))
def subtract(a, c):
    return str(a) + " - " + str(c) + " = " + str(int(a) - int(c))
def multiply(a, c):
    return str(a) + " * " + str(c) + " = " + str(int(a) * int(c))
def divide(a, c):
    return str(a) + " / " + str(c) + " = " + str(int(int(a) / int(c)))

if o == '+':
    print(add(a, c))
elif o == '-':
    print(subtract(a, c))
elif o == '*':
    print(multiply(a, c))
elif o == '/':
    print(divide(a, c))
else:
    print("False")