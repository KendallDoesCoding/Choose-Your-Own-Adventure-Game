# import modules
import subprocess
import sys

import pkg_resources

from chapters import *
from music_player import *

# install missing modules
required = {"playsound==1.2.2", "colorama==0.4.6"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, "-m", "pip", "install", *missing],
                          stdout=subprocess.DEVNULL)

# import dependencies

# heading text!
heading = "Choose Your Own Adventure Game!"
copyright = "\U000000A9 2023, KendallDoesCoding, All Rights Reserved"
new_str = Fore.BLUE + heading.center(150)
new_str2 = Fore.BLUE + copyright.center(150)
print(new_str)
print(new_str2)


def main():
    # welcome to the game
    name = input(Fore.YELLOW + "Hello \U0001F44B, Please enter your Name \U0000270D : " + Fore.LIGHTBLUE_EX)
    print(Fore.LIGHTGREEN_EX + "Welcome", name, "\U0001F91D, to the Adventure!\n")

    # do you want to play?
    answer = input(Fore.YELLOW + "Are You Ready? (yes/no) : " +
                   Fore.LIGHTBLUE_EX).lower()
    if answer == "y" or answer == "yes":
        # starting the game
        print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
    if answer == "n" or answer == "no":
        print("See you later! \U0001F600")
        exit()
    # do you want music?
    answer = input(Fore.YELLOW + "Do you want music? \U0001F3B5 (yes/no) : " +
                   Fore.LIGHTBLUE_EX).lower()

    if answer == "y" or answer == "yes":
        music()
        start()
    if answer == "n" or answer == "no":
        print(Fore.LIGHTGREEN_EX + "Okay \U0001F600 \n")
        start()


if __name__ == "__main__":
    main()
