class node:
    def __init__(self, d):
        self.p = None
        self.n = None
        self.d = d

class DDL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, num):
        nd = node(num)
        if self.head == None: # head가 null이면 자동으로 tail도 비어있음 -> 왜냐면 값이 들어있다면 둘 다 할당이 되기 때문에 
            self.head = nd
            self.tail = nd
        else:
            self.head.p = nd
            nd.n = self.head
            self.head = nd
        self.size += 1
    
    def push_back(self, num):
        nd = node(num)
        if self.tail == None:
            self.tail = nd
            self.head = nd
        else:
            self.tail.n = nd
            nd.p = self.tail
            self.tail = nd
        self.size += 1
    
    def pop_front(self):
        result = self.head
        if self.head.n == None:
            self.head = None
            self.tail = None
        else:
            self.head.n.p = None
            self.head = self.head.n
        self.size -= 1
        return result.d
    
    def pop_back(self):
        result = self.tail
        if self.tail.p == None:
            self.tail = None
            self.head = None
        else:
            self.tail.p.n = None
            self.tail = self.tail.p
        self.size -= 1
        return result.d
    
    def getSize(self):
        return self.size
    
    def empty(self):
        return 1 if self.size == 0 else 0
    
    def front(self):
        return self.head.d
    
    def back(self):
        return self.tail.d

n = int(input())

ddl = DDL()

for i in range(n):
    commands = input().split()
    if commands[0] == 'push_back':
        ddl.push_back(commands[1])
    elif commands[0] == 'push_front':
        ddl.push_front(commands[1])
    elif commands[0] == 'pop_back':
        r = ddl.pop_back()
        print(r)
    elif commands[0] == 'pop_front':
        r = ddl.pop_front()
        print(r)
    elif commands[0] == 'size':
        r = ddl.getSize()
        print(r)
    elif commands[0] == 'empty':
        r = ddl.empty()
        print(r)
    elif commands[0] == 'front':
        r = ddl.front()
        print(r)
    elif commands[0] == 'back':
        r = ddl.back()
        print(r)