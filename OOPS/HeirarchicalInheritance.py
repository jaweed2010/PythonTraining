class Shape:
    def calculate_area(self, dim):
        pass


class Rectangle(Shape):
    def calculate_area(self, rad):
        return 3.14 * rad * rad


class Square(Shape):
    def calculate_area(self, lnth):
        return lnth * lnth


class Rhombus(Shape):
    def calculate_area(self, p, q=1):
        return p*q/2


rect = Rectangle()
print(rect.calculate_area(5))
sq = Square()
print(sq.calculate_area(5))
rhom = Rhombus()
print(rhom.calculate_area(5))
