name = input("Hey, what's your name? ")
age = int(input("Ok, "+ name +", how old are you?"))
if age < 16 :
    print("you can't drive")
elif age < 18 :
    print("You can drive but not vote.")
elif age < 21 :
    print("You can vote but not rent a car.")
elif age >= 21 :
    print("You can do pretty much anything.")
