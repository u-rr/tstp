import math

# 1
class Apple:
    def __init__(self, w,c,b,d):
        self.weight: int = w
        self.color: str = c
        self.born: str = b
        self.day: int = d

# apple1 = Apple(4, "red","nagano",20200721)
# print(apple1.weight,apple1.color,apple1.born,apple1.day)

# 2
class Circle:
    def __init__(self,r):
        self.radius =r
        
    def area(self):
        return self.radius **2 * math.pi
        
cirlce = Circle(10)
print(cirlce.area())

# 3
class Triangle:
    def __init__(self, w,h):
        self.width = w
        self.height = h
        
    def area(self):
        return self.width * self.height /2
        
triangle = Triangle(10, 8)
print(triangle.area())

# 4
class Hexagon:
    def __init__(self):
        self.count = 6
        
    def calculate_perimeter(self, l):
        return l * self.count
        
hexagon = Hexagon()
print(hexagon.calculate_perimeter(20))
