import random
health = 100
badhealth = 100
power = 20
defense = 0
badpower = 30
baddefense = 0
while True:
    print("\nYour health is:" + str(health))
    print("Your enemies health is:" + str(badhealth))

    userinput = input("attack or fortify or calm mind\n")
    if userinput == "attack":
        badhealth -= power
    elif userinput == "fortify":
        defense += 10
    elif userinput == "calm mind":
        power += 5
        defense += 5
    elif userinput == "quit":
        print("BYEBYE")
        break
    else: 
        print("invalid")
        continue
    
    if badhealth <= 0:
        print("you win!")
        break

    enemy_choice = random.randrange(1,4)
    if enemy_choice == 1:
        health -= badpower
        print("\nenemy used attack")
    elif enemy_choice == 3:
        baddefense += 10
        print("\nenemy used fortify")
    elif enemy_choice == 2:
        badpower += 5
        baddefense += 5
        print("\nenemy used calm mind")
    else:
        print("that wasn't supposed to happen but you get a free turn ig")
    if health <= 0:
        print("you dead")
        break