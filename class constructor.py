class Student:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return (self.width*self.height)
    def sejal(self):
         print(f"the rectange having height:{self.height} and width: {self.width}")
student1=Student(3,4)
student2=Student(5,6)
student1.sejal()  
student2.sejal()
student1.area() 
print(student2.area())  
print(student1.area())  