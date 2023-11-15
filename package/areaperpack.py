from graphics import rectangle
from graphics import circle
from graphics.secondgraphics import cubiod
from graphics.secondgraphics import sphere
'''length=int(input("enter length"))
breadth=int(input("enter breadth"))
print("area of rectangle is:",rectangle.area(length,breadth))
print("perimeter of rectangle is:",rectangle.perimeter(length,breadth))
side=int(input("enter the side"))
print("area of circle is:",circle.area(side))
print("perimeter of circle is:",circle.perimeter(side))'''
length=int(input("enter length of cubeoid"))
breadth=int(input("enter breadth of cubeoid"))
height=int(input("enter height of cubeoid"))
print("area of cuboid is:",cubiod.surfacearea(length,breadth,height))
print("perimeter of cubeoid is:",cubiod.perimeter(length,breadth,height))
radius=int(input("enter the radius of the sphere"))
print("area of sphere is:",sphere.area(radius))
print("perimeter of sphere is:",sphere.perimeter(radius))
