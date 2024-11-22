def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()
    #it is designed to loop until given a valid input