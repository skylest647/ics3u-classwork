import random
list = []
for i in range (1000):
    list.append(random.randrange(10,100))
for e in range (list.__len__()):
    print(str(list[e]), end= "  ")