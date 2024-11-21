import random
drinks = 3
miles =  0
thirst = 0
exhaustion = 0
baddistance = -20
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your \ndesert trek and out run the natives.")

while True :
    if miles >= 200:
        print("You Win")
        break
    print("A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.\n")
    if exhaustion > 8:
        print("Your camels dead")
        break
    elif exhaustion > 5:
        print("your camel is tired")
    if thirst >= 6:
        print("You died of thirst")
        break
    elif thirst > 4:
        print("You are thirsty.")
    if miles <= baddistance:
        print("you got caught")
        break
    elif miles - baddistance <= 15:
        print("the natives are getting close")
    oasischance = random.randrange(1,21)
    if oasischance == 1:
        print('you found an oasis')
        thirst = 0
        drinks = 3
    choice = input()
    if choice.upper() == "A":
        if drinks > 0:
            thirst = 0
            drinks -= 1
        else:
            print("You cannot drink becasue you have no more drinks")
    elif choice.upper() == 'B':
        thirst += 1
        miles += random.randrange(5,12)
    elif choice.upper() == 'C':
        miles += random.randrange(10,20)
        thirst += 2
        exhaustion += random.randrange(1,4)      
        baddistance += random.randrange(7,15)
    elif choice.upper() == 'D':
        drinks += 3
        exhaustion = 0
        thirst = 0
        baddistance += 10
        print("The camel is happy")
        move = random.randrange(7,15)
        baddistance += move
        print(f"The native are {move} miles closer")
    elif choice.upper() == 'E':
        print("drinks:" + str(drinks))
        print("miles travelled:" + str(miles))
        print("The natives are "+ str(miles - baddistance) +" miles behind you.")
    elif choice == 'Q' or 'q':
        break
    else:
        print("Invalid input")
        