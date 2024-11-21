cat = 0
dog = 0
strin = str(input("give string: "))
for i in range (len(strin)):
    if strin[i].__contains__("c"):
        if strin[i+1].__contains__("a"):
            if strin[i+2].__contains__("t"):
                cat += 1
    if strin[i].__contains__("d"):
        if strin[i+1].__contains__("o"):
            if strin[i+2].__contains__("g"):
                dog += 1

print(cat == dog)