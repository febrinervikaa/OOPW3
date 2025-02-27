class Shape:
    width = 0 
    def __init__(self, width):
        self.width = width

class Square (Shape):
    nama = "Square"
    def get_area(self):
        return self.width ** 2
    
class Triangle(Shape):
    name = "Triangle"
    height = 0
    def __init__(self, width, height): 
        super().__init__(width)
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height
    
SquareX = Square(5)
TriangleY = Triangle(5, 3)

print("Luas Square:", SquareX.get_area())
print("Luas Triangle:", TriangleY.get_area())
