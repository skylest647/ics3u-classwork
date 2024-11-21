
numba = [1,2,3,4,5,6,7,8,9]
option = int(input("To find:"))
for i in range(numba.__len__()):
    if numba[i] == option:
        print(str(numba[i])+ " is in the list")