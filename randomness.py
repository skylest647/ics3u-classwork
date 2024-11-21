import random
random.seed(400)
#If changed to 1-5 it will change the random number to only 1,2,3,4,5 no more 6
x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")
#the numbers are the same even after re running the program
#When the seed changes the numbers change however its still the same after rerunnning it
#by doing it with the seed you can ensure the user gets the same results even after resetting which can prevent users from resetting the game to get better results
print()
print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")