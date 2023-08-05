
def Triangle():
    print("Triangle Area")
    hight = float(input("Inter the Height"))
    base = float(input("Inter the Base"))
    Triangle_Area = .5 * hight * base
    print(Triangle_Area)
    if Triangle_Area >= 10:
        print("Area is Height")
    elif Triangle_Area < 10 and Triangle_Area >0:
        print("Area is low")
    elif Triangle_Area <= 0:
        print("invalid input")
Triangle()
def circle():
    print("Circle Area")
    radius = float(input("Inter the Radius"))
    Circle_Area = 3.14*radius**2
    print(Circle_Area)
    if Circle_Area >= 10:
        print("Area is Height")
    elif Circle_Area < 10 and Circle_Area >0:
        print("Area is low")
    elif Circle_Area <= 0:
        print("invalid input")
circle()

def Rectangular():
    print("Rectangular_Area")
    side = float(input("Inter the Side"))
    wide = float(input("inter the wide"))
    rectangular_area = side*wide
    print(rectangular_area)
    if rectangular_area >= 10:
        print("Area is Height")
    elif rectangular_area < 10 and rectangular_area >0:
        print("Area is low")
    elif rectangular_area <= 0:
        print("invalid input")
Rectangular()


