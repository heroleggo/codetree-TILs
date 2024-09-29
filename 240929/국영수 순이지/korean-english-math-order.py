class a:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
    
    def p(self):
        print('{} {} {} {}'.format(self.name, self.kor, self.eng, self.mat))

n = int(input())
data = []

for i in range(n):
    [name, kor, eng, mat] = input().split()
    data.append(a(name, int(kor), int(eng), int(mat)))

data.sort(key=lambda x: (-x.kor, -x.eng, -x.mat))

for i in data:
    i.p()