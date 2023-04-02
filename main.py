# import modules
# Set the taskbar icon to same as pygame window icon
import ctypes
import os
import subprocess
import sys

import pkg_resources
import pygame

import music_player
from chapters import *
from GUI.GUI import GUIInstance

myappid = "KendallDoesCoding.ChooseYourAdventureGame.1.0"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# install missing modules
required = {"colorama==0.4.6", "pygame==2.2.0"}
installed = {pkg.key for pkg in pkg_resources.working_set}
if missing := required - installed:
    python = sys.executable
    subprocess.check_call([python, "-m", "pip", "install", *missing],
                          stdout=subprocess.DEVNULL)

# import dependencies
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
RUN_GUI = True

try:
    WINDOW = pygame.display.set_mode((SCR_W, SCR_H))
    print(Fore.RED + "Game opened with Pygame!")
except Exception as e:
    RUN_GUI = False
    print(Fore.RED + "Running without pygame")

pygame.display.set_caption("Choose Your Own Adventure")
pygame.display.set_icon(
    pygame.image.load("assets/images/logo.png"))  # SET PYGAME WINDOW ICON


def main():
    if RUN_GUI:
        GUIInstance.set_params(SCR_W, SCR_H, WINDOW)
        music_player.music()
    else:
        GUIInstance.set_params_no_gui()

    GUIInstance.start_screen()
    random.choice(my_list)()


if __name__ == "__main__":
    main()
