import random

# import the colorama module
import colorama
from colorama import Fore

import music.musicTimer as musicTimer  # stop music thread in this file
from music_player import *
from GUI.GUI import GUIInstance

colorama.init(convert=True)

# start the game

# Not called anywhere
def start():
    if GUIInstance.ask_question("You are on a dirt road. Which way to you want to go left or right?", "Left", "Right"):
        random.choice(my_list)()
    else:
        random.choice(my_list)()


# Not called anywhere

def chapter_river():
    if GUIInstance.ask_question("You come to a river, you can walk around it or swim across.", "Walk", "Swim"):
        # 1. Walk
        if GUIInstance.ask_question("You walked for many miles, ran out of water and remembered that there was a shop far away (10 miles/16kms) which supplies water. Do you want to go there?", "Yes", "No"):
            # 2. Yes
            if GUIInstance.ask_question("You went 10 miles walking and bought 10 liters of drinking water. Do you want to drink the water?", "Yes", "No"):
                # 3. Yes
                GUIInstance.text_until_enter("You drank 5 liters of water and now you feel refreshed.")
                if GUIInstance.ask_question("Do you want to walk further or go back home?", "Further", "Home"):
                    # 4. Further
                    game_over("You walked 100 more miles and you WIN the game! \U0001f3c6")
                else:
                    # 4. Home
                    game_over("A car crashed you and you were rushed to hospital. Although, it was too late by the time you reached the hospital, and you had already died. \U0001F480")

            else:
                # 3. No
                game_over("You died of thirst.\U0001F480")

        else:
            # 2. No
            game_over("You were very de-hydrated and died of thirst when you were walking. \U0001F480")

    else:
        # 1. Swim
        game_over("You swam across the river and were eaten by an aligator \U0001F480")



def chapter_bridge():
    if GUIInstance.ask_question("You come to a bridge, it looks wobbly. Do you want to cross it or do you want to head back?", "Cross", "Back"):
        # 1. Cross
        chapter_stranger()
    
    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            game_over("You drive forward and crash into a tree and die.\U0001F480")
        else:
            # 2. Left
            chapter_lake()


def chapter_stranger():
    if GUIInstance.ask_question("You cross the bridge and meet a stranger, do you talk to them?", "Yes", "No"):
        # 1. Yes
        if GUIInstance.ask_question("You talk a wizard and he asks you, do you want to be a wizard?", "Yes", "No"):
            # 2. Yes
            game_over("You are a wizard and you WIN the game! \U0001f3c6")
        else:
            # 2. No
            game_over("The stranger was not pleased by you and murdered you. \U0001F480")
    else:
        # 1. No
        game_over("The stranger was not pleased by you and murdered you. \U0001F480")


def chapter_lake():
    if GUIInstance.ask_question("You turned left and you come to a lake, do you want to swim or go back?", "Swim", "Back"):
        # 1. Swim
        game_over("You swam across the lake and were eaten by a shark. \U0001F480 ")
    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            chapter_tree()
        else:
            # 2. Left
            game_over("You died. \U0001F480")


def chapter_tree():
    if GUIInstance.ask_question("You are very hungry and you see a tree with apples, do you want to eat the fruit?", "Yes", "No"):
        # 1. Yes
        game_over("You ate the fruit but it was poisonous and you died. \U0001F480")
    else:
        # 1. No
        if GUIInstance.ask_question("You are nearly starving to death. Do you want to eat Pears instead of apples?", "Yes", "No"):
            # 2. Yes
            game_over("You ate the pears but they were poisonous and you died. \U0001F480")
        else: 
            # 2. No
            game_over("You were so hungry that you were nearly going to die in a few seconds, but a lovely gentleman gave you some food and you WIN the game! \U0001f3c6")


def game_over(message: str = None):
    "Shows Game over message"
    if message:
        GUIInstance.text_until_enter(message)
    
    if GUIInstance.ask_question("Thanks for playing!", "Play Again", "Quit"):
        # Play again
        random.choice(my_list)()
    else:
        # Quit
        musicTimer.musicTimerObj.cancel()  # stop music thread, make sure to call these 2 lines every time program exits
        musicTimer.musicTimerObj.join()

        exit()


my_list = [chapter_bridge, chapter_lake]
