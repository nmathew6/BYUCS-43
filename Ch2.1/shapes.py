import math

class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ('<'+ self.__class__.__name__ + ' Shape x=' + str(self.x) + ' y=' + str(self.y) +'>')

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return ('<'+self.__class__.__name__+' x=' +str(self.x) +' y=' + str(self.y) + ' radius='+str(self.radius) + '>')

    def circumference(self):
        return self.radius * 2 * math.pi

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def __repr__(self):
        return ('<'+self.__class__.__name__+' x=' +str(self.x) +' y=' + str(self.y) + ' length='+str(self.length) + ' width='+str(self.width)+'>')

    def area(self):
        return self.length * self.width

    def circumference(self):
        return (self.length * 2) + (self.width * 2)

class RightTriangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def __repr__(self):
        return ('<'+self.__class__.__name__+' x=' +str(self.x) +' y=' + str(self.y) + ' base='+str(self.base) + ' height='+str(self.height)+'>')

    def area(self):
        return self.base * 0.5 * self.height

    def circumference(self):
        return self.base + self.height + math.sqrt((self.base **2) + (self.height ** 2))

class Square(Rectangle):
    def __init__(self, x, y, length):
        super().__init__(x, y, length, length)

    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' x=' + str(self.x) + ' y=' + str(self.y) + ' length=' + str(self.length) + '>')



def processShape(shape):
    print("Area is "+str(shape.area()))
    print("Circumference is "+str(shape.circumference()))

circle_1 = Circle(2, 4, 5)
square_1 = Square(2,4, 7)
rectange_1 = Rectangle(1,3, 21, 1)
rtri_1 = RightTriangle(5, 2, 3, 4)

print (circle_1)
print (circle_1.area())
print (circle_1.circumference())
print()
print (square_1)
print (square_1.area())
print (square_1.circumference())
print()
print (rectange_1)
print (rectange_1.area())
print (rectange_1.circumference())
print()
print (rtri_1)
print (rtri_1.area())
print (rtri_1.circumference())


shapes = [circle_1,square_1,rectange_1,rtri_1]

for s in shapes:
    processShape(s)
    print("* * * * * * * ")





