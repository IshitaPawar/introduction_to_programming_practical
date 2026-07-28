import math
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))
area_rect=length*breadth
perimeter_rect=2*(length+breadth)

radius=float(input("enter radius:"))
area_circle=math.pi*radius**2
circumference=2*math.pi*radius

print("\nRectangle")
print("area=",area_rect)
print("perimeter=",perimeter_rect)

print("\nCircle")
print("area=",round(area_circle,2))
print("perimeter=",round(circumference,3))
