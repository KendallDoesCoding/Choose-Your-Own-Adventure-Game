from chapters import *
from music import * 

def main():
    # welcome to the game
    name = input(Fore.YELLOW + "Type your name: ")
    print("Welcome", name, "to this adventure!")

    # do you want to play?
    answer = input(Fore.YELLOW + "Do you want to play? (y/n) ")
    if answer == "y" or answer == "yes":
        # starting the game
        print("Let's play!")
    if answer == "n" or answer == "no":
        print("See you later!")
        exit()
    # do you want music?
    answer = input(Fore.YELLOW + "Do you want music? \U0001F3B5 (y/n) ")
    if answer == "y" or answer == "yes":
        music()
        start()
    if answer == "n" or answer == "no":
        print("Okay \U0001F600")
        start()



if __name__ == "__main__":
    main()


