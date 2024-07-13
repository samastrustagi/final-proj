import math




class Shape():
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def calculate_area(self):
        return self.length * self.breadth
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)
    
    
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    
    
    
radius = float(input("Please enter the radius of the Circle: "))   
circle = Circle(radius)
area_circle = circle.calculate_area()
perimeter_circle = circle.calculate_perimeter()
print(f"Area of the Circle is {area_circle}")
print(f"Perimeter of the Circle is {perimeter_circle}")


side = float(input("Please enter the Side of the Square: "))
square = Square(side)
area_square = square.calculate_area()
perimeter_square = square.calculate_perimeter()
print(f"Area of the Square is {area_square}")
print(f"Perimeter of the Square is {perimeter_square}")


length = float(input("Please enter the Length of the Rectangle: "))
breadth = float(input("Please enter the Breadth of the Rectangle: "))
rectangle = Rectangle(length, breadth)
area_rectahgnle = rectangle.calculate_area()
perimeter_rectangle = rectangle.calculate_perimeter()
print(f"Area of the Rectangle is {area_rectahgnle}")
print(f"Perimeter of the Rectangle is {perimeter_rectangle}")


base = float(input("Please enter the Base of the Triangle: "))
height = float(input("Please enter the Height of the Triangle: "))
side1 = float(input("Please enter the first side of the Triangle: "))
side2 = float(input("Please enter the second side of the Triangle: "))
side3 = float(input("Please enter the third side of the Triangle: "))
triangle = Triangle(base, height, side1, side2, side3)
area_triangle = triangle.calculate_area()
perimeter_triangle = triangle.calculate_perimeter()
print(f"Area of the Triangle is {area_triangle}")
print(f"Perimeter of the Triangle is {perimeter_triangle}")


# def main():
#     print(f"I can calculate Areas and Perimeters of the following shapes:- \n 1. Circle \n 2. Square \n 3. Rectangle \n 4. Triangle")
#     user_input = get_user_input()


# def get_user_input():
#     validate_user_input("Please enter 1, 2, 3 or 4. ")
    

# def validate_user_input(prompt):
#     while True:
#         try:
#             return 


# if __name__ == "__main__":
#     main()
