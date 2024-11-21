import random
random.seed(1)
random_num = random.randrange(1,11)
print("I'm thinking of a number from 1 to 10.")
guess = input("Your guess: ")
if guess == str(random_num):
    print("That's right!  My secret number was " + str(random_num) + "!")
else:
    print("Sorry, but I was really thinking of " + str(random_num) + ".")