class h:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    
    def p(self):
        print('{} {}'.format(self.n, self.s))

minS = 101

result = -1

for i in range(5):
    [n, s] = input().split()
    if int(s) < minS:
        result = h(n, s)
        minS = int(s)

result.p()