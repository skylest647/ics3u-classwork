import random
list = []
for i in range (10):
    list.append(random.randrange(1,101))
for e in range (list.__len__()):
    print("Slot " + str(e) + " contains a " + str(list[e]))