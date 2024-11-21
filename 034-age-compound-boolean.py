name = input("Your name: ")
age = input("Your age: ")
if age < 16:
    print("You can't drive.")
if age == 16 or 17:
    print("You can drive but not vote.")
if age == 18 or 24:
    print("You can vote but not rent a car.")
if age >= 25:
    print("You can do pretty much anything.")