numba = [1, 2, 3, 4, 5, 6, 7, 8, 9]
option = int(input("To find:"))
found = False

for i in range(len(numba)):
    if numba[i] == option:
        print(str(numba[i]) + " is in the list")
        found = True
        break

if not found:
    print("It's not in the list")