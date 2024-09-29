class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def p(self):
        print('product {} is {}'.format(self.code, self.name))

a = product('codetree', '50')

[n, c] = input().split()

b = product(n, c)

a.p()
b.p()