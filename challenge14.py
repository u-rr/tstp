class Square():
    square_list = []
    
    def __init__(self, w:int):
        self.width: int = w
        self.square_list.append(self.width)
        
    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.width,self.width,self.width,self.width)
        
    def calculate_perimeter(self):
        print(self.width * 4)
        
    def change_size(self, num: int):
        self.width += num
    
square1 = Square(5)
square2 = Square(7)
square3 = Square(29)

print(Square.square_list)
print(square3)

def three(one, two):
    print(one is two)

three(1, 1)
three(1,"1")
