
def Triangle():
    print("Triangle Area")
    h = int(input("inter the Height"))
    b = int(input("Inter the Base"))
    Triangle_Area = .5*h*b
    print(Triangle_Area)
Triangle()

def Square():
    print("Square Area and Perimeter")
    r = int(input("Inter the Rib"))
    Square_Area = r*r
    Square_Perimeter = r*4
    print(Square_Area)
    print(Square_Perimeter)
Square()

def Rectangle():
    print("Rectangle Area and Perimeter")
    l = int(input("Inter the Length"))
    w = int(input("Inter the Wide"))
    Rectangle_Area = l*w
    Rectangle_perimeter = l+l+w+w
    print(Rectangle_Area)
    print(Rectangle_perimeter)
Rectangle()