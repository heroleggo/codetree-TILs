class b:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def p(self):
        print('code : {}'.format(self.code))
        print('color : {}'.format(self.color))
        print('second : {}'.format(self.second))

[code, color, second] = input().split()

a = b(code, color, second)

a.p()