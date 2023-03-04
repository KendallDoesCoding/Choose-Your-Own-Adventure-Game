from chapters import *
from music import * 

music()

def main():
    # welcome to the game
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    # do you want to play?
    answer = input("Do you want to play? (y/n) ")
    if answer == "y" or answer == "yes":
        # starting the game
        print("Let's play!")
        # start the game
        start()

    if answer == "n" or answer == "no":
        print("See you later!")
        exit()



if __name__ == "__main__":
    main()

