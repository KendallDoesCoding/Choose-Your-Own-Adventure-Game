# import modules
import subprocess
import sys

import pkg_resources

from chapters import *
import music_player

from GUI.GUI import GUIInstance

# install missing modules
required = {"playsound==1.2.2", "colorama==0.4.6", "pygame==2.1.3.dev8"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, "-m", "pip", "install", *missing],
                          stdout=subprocess.DEVNULL)

# import dependencies
import pygame
pygame.init()

# heading text!


heading = "Choose Your Own Adventure Game!"
copyright = "\U000000A9 2023, KendallDoesCoding, All Rights Reserved"
new_str = Fore.BLUE + heading.center(150)
new_str2 = Fore.BLUE + copyright.center(150)
print(new_str)
print(new_str2)

SCR_W = 800
SCR_H = 600

WINDOW = pygame.display.set_mode((SCR_W, SCR_H))
pygame.display.set_caption("Choose Your Own Adventure")    


def main():
    GUIInstance.set_params(SCR_W, SCR_H, WINDOW)
    
    music_player.music()
    GUIInstance.start_screen()

    #TODO: Music toggle
    #TODO: Background

    # welcome to the game
    # name = input(Fore.YELLOW + "Type your name: " + Fore.LIGHTBLUE_EX)
    # print(Fore.LIGHTGREEN_EX + "Welcome", name, "to this adventure!")

    # # do you want to play?
    # answer = input(Fore.YELLOW + "Do you want to play? (y/n) " +
    #                Fore.LIGHTBLUE_EX)
    # if answer == "y" or answer == "yes":
    #     # starting the game
    #     print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
    # if answer == "n" or answer == "no":
    #     print("See you later! \U0001F600")
    #     exit()
    # # do you want music?
    # answer = input(Fore.YELLOW + "Do you want music? \U0001F3B5 (y/n) " +
    #                Fore.LIGHTBLUE_EX)
    # if answer == "y" or answer == "yes":
    #     random.choice(my_list)(GUI)
    # if answer == "n" or answer == "no":
    #     print(Fore.LIGHTGREEN_EX + "Okay \U0001F600")
    #     random.choice(my_list)(GUI)

    random.choice(my_list)()


if __name__ == "__main__":
    main()
