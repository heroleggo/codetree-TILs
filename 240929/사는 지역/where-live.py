class info:
    def __init__(self, name, addr, region):
        self.name = name
        self.addr = addr
        self.region = region
    
    def p(self):
        print('name {}'.format(self.name))
        print('addr {}'.format(self.addr))
        print('city {}'.format(self.region))

n = int(input())

default = 'a'
result = -1

for i in range(n):
    [name, addr, region] = input().split()
    if name > default:
        default = name
        result = info(name, addr, region)

result.p()