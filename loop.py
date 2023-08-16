def sum (num1,num2):
    print(f"{num1} + {num2}= ",num1+num2)
def subtract (num1,num2):
    print(f"{num1} - {num2}= ", num1 - num2)
def multiply(num1,num2):
    print(f"{num1} * {num2}= ", num1 * num2)
def division (num1,num2):
    print(f"{num1} / {num2}= ", num1 / num2)
def triangle_area (base,length):
    print("Trianglr Area= ",.5 * b * l)
def circlr_area (radius):
    print("Circle Area= ",3.14 * r * r)
def rectangle_area (Length,width):
    print("Rectangle Area= ",le * w)


while True :
    selections = int(input(f"""1. Sum
2. Subtract
3. Multiply
4. Division
5. Calculate triangle area
6. Calculate circle area
7. Calculate rectangle area
8. Exit"""))
    if selections == 1:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
    sum(num1=num1,num2=num2)

    elif selections == 2:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
    subtract(num1=num1,num2=num2)

    elif selections == 3:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
    multiply(num1=num1,num2=num2)
    elif selections == 4:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
    division(num1=num1,num2=num2)
    elif selections == 5:
        b = float(input("inter the Triangle Base "))
        l = float(input("inter the Triangle length "))
    triangle_area(base=b,length=l)
    elif selections == 6:
        r = float(input("inter the Circle Radius "))
    circlr_area(raduis=r)
    elif selections == 7:
        le = float(input("inter rectangle Length "))
        w = float(input("inter rectangle width "))
    rectangle(length=le,width=w)
    elif selections == 8:
        exit()
    else:
        print("Invalid Input")