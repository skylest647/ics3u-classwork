name = input("Hey, what's your name? ")
age = int(input("Ok, "+ name +", how old are you?"))
if age < 16 :
    print("you can't drive")
if age < 18 :
    print("you can't vote")
if age < 21 :
    print("you can't rent a car")
if age >= 21 :
    print("You can do anything that's legal.")
