class A:
    def addn(self, a, b):
        return a + b

    def subt(self, a, b):
        return a - b


class B(A):
    def mult(self, a, b):
        return a * b

    def __str__(self):
        return

o = B()
print(o.addn(3, 5))
print(o.subt(3, 5))
print(o.mult(3, 5))
print(o.__str__())