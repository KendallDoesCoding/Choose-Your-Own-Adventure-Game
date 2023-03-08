from chapters import *
from music import * 

txt = 'Choose Your Own Adventure Game!'
txt2 = "\U000000A9 2023, KendallDoesCoding, All Rights Reserved"
new_str = Fore.BLUE + txt.center(150)
new_str2 = Fore.BLUE + txt2.center(150)
print(new_str)
print(new_str2)


def main():
    # welcome to the game
    name = input(Fore.YELLOW + "Type your name: ")
    print(Fore.LIGHTGREEN_EX + "Welcome", name, "to this adventure!" )

    # do you want to play?
    answer = input(Fore.YELLOW + "Do you want to play? (y/n) ")
    if answer == "y" or answer == "yes":
        # starting the game
        print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
    if answer == "n" or answer == "no":
        print("See you later! \U0001F600")
        exit()
    # do you want music?
    answer = input(Fore.YELLOW + "Do you want music? \U0001F3B5 (y/n) ")
    if answer == "y" or answer == "yes":
        music()
        start()
    if answer == "n" or answer == "no":
        print(Fore.LIGHTGREEN_EX + "Okay \U0001F600")
        start()



if __name__ == "__main__":
    main()


