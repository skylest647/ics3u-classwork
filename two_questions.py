userinput = input("animal, vegetable, or mineral?\n")
sinput = input("is it bigger than a breadbox?\n")
if userinput == "animal":
    if sinput == "yes":
        print("My guess is that you are thinking of a moose.")
    elif sinput == "no":
        print("My guess is that you are thinking of a squirrel.")
elif userinput == "vegetable":
    if sinput == "yes":
        print("My guess is that you are thinking of a watermelon.")
    elif sinput == "no":
        print("My guess is that you are thinking of a carrot.")
elif userinput == "mineral":
    if sinput == "yes":
        print("My guess is that you are thinking of a Camaro.")
    elif sinput == "no":
        print("My guess is that you are thinking of a paper clip.")
