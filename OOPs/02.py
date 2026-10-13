'''
Insatance methods : Rectangle area and perimeter
Problem: Create a Rectangle class with length and breadth. Use instance methods to calculate its area and perimeter
'''
class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

r = rectangle(length,breadth)
print(f"Area of rectangle is {r.area()}")
print(f"Perimeter of rectangle is {r.perimeter()}")