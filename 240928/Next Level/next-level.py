class u:
    def __init__(self, i, l):
        self.i = i
        self.l = l
    
    def p(self):
        print("user {} lv {}".format(self.i, self.l))

a = u("codetree", "10")
[i, l] = input().split()
b = u(i, l)

a.p()
b.p()