class Rectangle:
    def set_dimensions(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2*(self.height*self.width)
rectangle=Rectangle()
rectangle.set_dimensions(4,3)

print(rectangle.area())
print(rectangle.perimeter())
print("the height and width are:",rectangle.height,rectangle.width)