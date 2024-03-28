class Arith:
    def __int__(self,a):
        self.a=a
    def addn(self, a, b):
        return a + b

    def subn(self, a, b):
        return a - b


o = Arith()
print("addition is", o.addn(1, 2))
print("subt is", o.subn(1, 2))
