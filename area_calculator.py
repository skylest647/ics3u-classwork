import math

def area_circle (radius: int)-> float:
    return math.pi * (radius ** 2)

def area_rectangle(length: float, width: float) -> float:
    return length * width

def area_square(side: float)-> float:
    return side ** 2

def area_triangle (base: float, height: float) -> float:   
    return 0.5 * base * height

while True:
    print("1) Triangle \n2) Rectangle \n3) Square \n4) Circle \n5) Quit")
    uinput = int(input("Which shape: "))
    if uinput == 1:
        base = float(input("base: "))
        height = float(input("height"))
        print("The area is " + str(area_triangle(base,height)))
    elif uinput == 2:
        length = float(input("length: "))
        width = float(input("width"))
        print("The area is " + str(area_rectangle(length, width)))
    elif uinput == 3:
        side = float(input("side"))
        print("The area is " + str(area_square(side)))
    elif uinput == 4:
        radius = float(input("radius"))
        print("The area is " + str(area_circle(radius)))
    elif uinput == 5:
        print("Goodbye")
        break
    else: 
        print("not valid input")