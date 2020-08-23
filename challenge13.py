class Shape:
    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    def __init__(self, w:int, l:int):
        self.width: int = w
        self.len: int = l
        
    def calculate_perimeter(self):
        print((self.width + self.len) * 2)

class Square(Shape):
    def __init__(self, w:int):
        self.width: int = w
        
    def calculate_perimeter(self):
        print(self.width * 4)
        
    def change_size(self, num: int):
        self.width += num

rectangle = Rectangle(4,7)
square = Square(5)

rectangle.calculate_perimeter()
square.calculate_perimeter()
square.change_size(10)
print(square.width)

rectangle.what_am_i()
square.what_am_i()

class Horse:
    def __init__(self, owner):
        self.owner: str = owner

class Rider:
    def __init__(self, name):
        self.name: str = name
        
rider1 = Rider('rina')
horse = Horse(rider1)

print(horse.owner.name)
