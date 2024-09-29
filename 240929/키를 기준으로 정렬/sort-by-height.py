class info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def p(self):
        print('{} {} {}'.format(self.name, self.height, self.weight))

n = int(input())
data = []

for i in range(n):
    [name, height, weight] = input().split()
    data.append(info(name, int(height), int(weight)))

data.sort(key=lambda x: x.height)

for i in data:
    i.p()