# import modules
import subprocess
import sys
import pkg_resources
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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
import colorama

# heading text!
ImageAddress = 'assets/images/logo.png'
ImageAddress = 'assets\images/logo.png'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)
plt.imshow(ImageNumpyFormat)
plt.draw()
plt.pause(1) # pause how many seconds
plt.close()

# heading text!
heading = "Choose Your Own Adventure Game!"
copyright = "\U000000A9 2023, KendallDoesCoding, All Rights Reserved"
new_str = Fore.BLUE + heading.center(150)
new_str2 = Fore.BLUE + copyright.center(150)
print(new_str)
print(new_str2)


def main():
    # welcome to the game
    name = input(Fore.YELLOW + "Type your name: " + Fore.LIGHTBLUE_EX)
    print(Fore.LIGHTGREEN_EX + "Welcome", name, "to this adventure!")

    # do you want to play?
    answer = input(Fore.YELLOW + "Do you want to play? (y/n) " +
                   Fore.LIGHTBLUE_EX)
    if answer == "y" or answer == "yes":
        # starting the game
        print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
    if answer == "n" or answer == "no":
        print("See you later! \U0001F600")
        exit()
    # do you want music?
    answer = input(Fore.YELLOW + "Do you want music? \U0001F3B5 (y/n) " +
                   Fore.LIGHTBLUE_EX)
    if answer == "y" or answer == "yes":
        music()
        random.choice(my_list)()
    if answer == "n" or answer == "no":
        print(Fore.LIGHTGREEN_EX + "Okay \U0001F600")
        random.choice(my_list)()


if __name__ == "__main__":
    main()
