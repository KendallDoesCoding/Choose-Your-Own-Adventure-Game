# import modules
import subprocess
import sys

# Set the taskbar icon to same as pygame window icon
import ctypes
myappid = 'KendallDoesCoding.ChooseYourAdventureGame.1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pkg_resources

from chapters import *
import music_player

from GUI.GUI import GUIInstance

# install missing modules
required = {"colorama==0.4.6", "pygame==2.2.0"}
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
RUN_GUI = True

try:
    WINDOW = pygame.display.set_mode((SCR_W, SCR_H))
except Exception as e:
    RUN_GUI = False
    print(f"Running without pygame")

pygame.display.set_caption("Choose Your Own Adventure") 
pygame.display.set_icon(pygame.image.load("assets/images/logo.png"))    # SET PYGAME WINDOW ICON


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
