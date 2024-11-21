number = 0
strin = str(input("give string: "))
for i in range (len(strin)):
    if strin[i].__contains__("h"):
        if strin[i+1].__contains__("i"):
            number += 1
print(number)