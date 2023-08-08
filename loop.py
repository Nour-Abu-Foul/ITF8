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
        s = num1 + num2
        print("Result:", s)
    elif selections == 2:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
        su = num1 - num2
        print("Result: ", su)
    elif selections == 3:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
        m = num1 * num2
        print("Result: ", m)
    elif selections == 4:
        num1 = float(input("inter first number "))
        num2 = float(input("inter second number "))
        d = num1/num2
        print("Result: ",d)
    elif selections == 5:
        b = float(input("inter the Triangle Base "))
        l = float(input("inter the Triangle length "))
        ta = .5 * b * l
        print("Triangle Area: ",ta)
    elif selections == 6:
        r = float(input("inter the Circle Radius "))
        cr = 3.14 * r * r
        print("Circle Area: ",cr)
    elif selections == 7:
        le = float(input("inter rectangle Length "))
        w = float(input("inter rectangle width "))
        ra = le * w
        print("Rectangle Area: ",ra)
    else:
        break