import math


class Shape_3D():
    def calculate_volume(self):
        pass
    
    
class Sphere(Shape_3D):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_volume(self):
        return 4/3 * math.pi * self.radius ** 3
    

class Hemisphere(Shape_3D):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_volume(self):
        return 2/3 * math.pi * self.radius ** 3
    
    
class Cube(Shape_3D):
    def __init__(self, side):
        self.side = side
        
    def calculate_volume(self):
        return self.side ** 3
    
    
class Cuboid(Shape_3D):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def calculate_volume(self):
        return self.length * self.breadth * self.height
    

class ShapeWithRadiusHeight(Shape_3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
        
class Cone(ShapeWithRadiusHeight):
    def __init__(self, radius, height):
        super().__init__(radius, height)
        
    def calculate_volume(self):
        return 1/3 * math.pi * self.radius ** 2 * self.height
    

class Cylinder(ShapeWithRadiusHeight):
    def __init__(self, radius, height):
        super().__init__(radius, height)
        
    def calculate_volume(self):
        return math.pi * self.radius ** 2 * self.height
    
    
    

radius = float(input("Please enter the Radius of the Sphere: "))
sphere = Sphere(radius)
volume_sphere = sphere.calculate_volume()
print(f"The volume of the Sphere is {volume_sphere}")

radius = float(input("Please enter the Radius of the Hemisphere: "))
hemisphere = Hemisphere(radius)
volume_hemisphere = hemisphere.calculate_volume()
print(f"The volume of the Hemisphere is {volume_hemisphere}")

side = float(input("Please enter the Side of the Cube: "))
cube = Cube(side)
volume_cube = cube.calculate_volume()
print(f"The volume of the Cube is {volume_cube}")

length = float(input("Please enter the length of the Cuboid: "))
breadth = float(input("Please enter the breadth of the Cuboid: "))
height = float(input("Please enter the height of the Cuboid: "))
cuboid = Cuboid(length, breadth, height)
volume_cuboid = cuboid.calculate_volume()
print(f"The volume of the Cuboid is {volume_cuboid}")

radius = float(input("Please enter the radius of the Cone: "))
height = float(input("Please enter the height of the Cone: "))
cone = Cone(radius, height)
volume_cone = cone.calculate_volume()
print(f"The volume of the Cone is {volume_cone}")

radius = float(input("Please enter the radius of the Cylinder: "))
height = float(input("Please enter the height of the Cylinder: "))
cylinder = Cylinder(radius, height)
volume_cylinder = cylinder.calculate_volume()
print(f"The volume of the Cylinder is {volume_cylinder}")
