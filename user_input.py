print("Enter the following information about an item you wish to purchase..")
print()

#no float conversion

name = input("The name of the item:")

#Converted to a float
price = float(input("The price: $"))

quantity = int(input("How many do you want?"))
#changing the order will wait for user input before asking for user input
subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#int and float functions are needed as you need to classify what the input should be such as a string, integer and float respectively