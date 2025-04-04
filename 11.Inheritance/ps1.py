class C:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        print(f"The 2d vector is {self.a}i+ {self.b}j")

class C11(C):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
    def show(self):
        print(f"The 3d vector is {self.a}i+ {self.b}j + {self.c}k")

m = C(1,2)
m.show()
n = C11(5,6,3)
n.show()


