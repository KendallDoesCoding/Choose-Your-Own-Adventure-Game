# import modules
import subprocess
import sys

import time

import pkg_resources
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from chapters import *
from music_player import *
from GUIObjects import Button, TextBox
from GUIFuncs import seperate_text_to_rows

# install missing modules
required = {"playsound==1.2.2", "colorama==0.4.6"}
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


ImageAddress = 'assets\images/logo.png'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)
plt.imshow(ImageNumpyFormat)
plt.draw()
plt.pause(1) # pause how many seconds
plt.close()
heading = "Choose Your Own Adventure Game!"
copyright = "\U000000A9 2023, KendallDoesCoding, All Rights Reserved"
new_str = Fore.BLUE + heading.center(150)
new_str2 = Fore.BLUE + copyright.center(150)
print(new_str)
print(new_str2)

SCR_W = 800
SCR_H = 800

WINDOW = pygame.display.set_mode((SCR_W, SCR_H))
pygame.display.set_caption("Choose Your Own Adventure")

player_name = ""
BG_COLOR = (128, 255, 0)
FONT = pygame.font.Font(None, 60)

def start_sequence():
    text_box_w = 300
    text_box_h = 100
    name_text_box = TextBox((SCR_W / 2 - text_box_w / 2, SCR_H / 2 - text_box_h / 2, text_box_w, text_box_h), font=FONT)    
    
    text = FONT.render("Hi! What is you name?", True, (0,0,0))

    got_name = False

    while (not got_name):
        WINDOW.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            name_text_box.get_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = "".join(name_text_box.buffer)
                    got_name = True
        
        WINDOW.blit(text, (SCR_W / 2 - text.get_size()[0] / 2, SCR_H/2 + 100))
        name_text_box.update()
        name_text_box.draw(WINDOW)
        pygame.display.update()

    text_list = seperate_text_to_rows(f"Welcome {player_name} to this adventure!", SCR_W - 50, FONT)

    _continue = False
    while (not _continue):
        WINDOW.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            name_text_box.get_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    _continue = True

        for _i, _text in enumerate(text_list):
            WINDOW.blit(_text, (SCR_W / 2 - _text.get_size()[0] / 2, (SCR_H/2  - _text.get_size()[1] / 2) + 40 * _i))

        #WINDOW.blit(text, (SCR_W / 2 - text.get_size()[0] / 2, SCR_H/2  - text.get_size()[1] / 2))

        pygame.display.update()

    print(player_name)

def main():
    button_left = Button(SCR_W * .25, SCR_H * .75, 200, 40, text="LEFT", font_size=32, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
    button_right = Button(SCR_W * .75, SCR_H * .75, 200, 40, text="RIGHT", font_size=32, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
    buttons = [button_left, button_right]
    
    start_sequence()

    while(True):
        WINDOW.fill(BG_COLOR)
        

        for btn in buttons:
            btn.draw(WINDOW)
            btn.check_hover(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for btn in buttons:
                        if btn.check_click():
                            print("clicked")

        pygame.display.update()
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
