area_s = lambda a:a*a
area_rect=lambda l,b:l*b
area_triangle=lambda b1,h:0.5*b1*h
a=int(input("enter the side of the square"))
print("area of square",area_s(a))
l=int(input("enter the length of the rectangle"))
b=int(input("enter the breadth of the rectangle"))
print("area of square",area_rect(l,b))
b1=int(input("enter the base of the triangle"))
h=int(input("enter the height of the triangle"))
print("area of triangle",area_triangle(b1,h))
