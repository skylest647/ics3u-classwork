import random
import os
import time

def main():
    for i in range(100000):
        r = random.randrange(1, 6)
        if r is 1:
            first()
        elif r is 2:
            second()
        elif r is 3:
            third()
        elif r is 4:
            fourth()
        elif r is 5:
            fifth()
        else:
            print("how???")
        time.sleep(1)
        os.system("clear")  # clear console

    print("I pledge allegiance to the flag.");


def first():
    print("I                               ");


def second():
    print("  pledge                        ");


def third():
    print("         allegiance             ");


def fourth():
    print("                    to the      ");


def fifth():
    print("                           flag.");


if __name__ == "__main__":
    main()