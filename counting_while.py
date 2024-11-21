print("Type in a message, and I'll display it several times.")

message = input("Message: ")
print()
times = int(input("how many times?"))
n = 1
while n <= times:
    print(f"{n * 10}. {message}")
    n += 1