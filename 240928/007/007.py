class hehe:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p(self):
        print("secret code :", self.a)
        print("meeting point :", self.b)
        print("time :", self.c)

[x, y, z] = input().split()

h = hehe(x, y, z)

h.p()