import random

# import the colorama module
import colorama
from colorama import Fore

import music.musicTimer as musicTimer  # stop music thread in this file
from music_player import *

colorama.init(convert=True)

# start the game


def start():
    answer = input(
        Fore.GREEN +
        "You are on a dirt road. Which way do you want to go left or right? " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs left then
    if answer == "left":
        random.choice(my_list)()

    # if user inputs right then
    if answer == "right":
        random.choice(my_list)()


def chapter_river():
    answer = input(
        Fore.GREEN +
        "You come to a river, you can walk around it or swim across."
        "Type walk to walk around & swim to swim across. " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs swim then
    if answer == "swim":
        game_over(
            Fore.RED +
            "You swam across the river and were eaten by an alligator \U0001F480"
        )
    # if user inputs walk then
    elif answer == "walk":
        # q2
        answer = input(
            Fore.GREEN +
            "You walked for many miles, ran out of water and remembered "
            "that there was a shop far away (10 miles/16kms) which supplies water."
            "Do you want to go there (yes/no)? " +
            Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs no then
        if answer == "no":
            game_over(
                Fore.RED +
                "You become de-hydrated and died of thirst when you were walking. \U0001F480"
            )

        # if user inputs yes then
        elif answer == "yes":
            print(
                Fore.GREEN +
                "You went 10 miles walking and bought 10 liters of drinking water. "
            )
            # q3
            answer = input(
                Fore.GREEN +
                "You are thirsty, do you want to drink some water (yes/no)? " +
                Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs yes then
        if answer == "yes":
            print(Fore.GREEN +
                  "You drank 5 liters of water and now you feel refreshed.")

        # if user inputs no then
        elif answer == "no":
            game_over(Fore.RED + "You died of thirst.\U0001F480 ")
        else:
            print(Fore.RED + "Not a valid answer. You die. \U0001F480")
            random.choice(my_list)()
        # q4
        answer = input(
            Fore.GREEN +
            "You drank 5 liters of water and now you feel refreshed. Do you want to walk further or go back home? (further/home) "
            + Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs further then
        if answer == "further":
            game_over(
                Fore.RED +
                "You walked 100 more miles and you WIN the game! \U0001f3c6",
                win=True,
            )
        # if user inputs home then
        if answer == "home":
            game_over(
                Fore.RED +
                "A car crashed you and you were rushed to hospital. Although, it was too late by the time you reached the hospital, and you had already died. \U0001F480"
            )
        else:
            print(Fore.RED + "Not a valid answer. You die. \U0001F480")
            game_over()


def chapter_bridge():
    answer = input(
        Fore.GREEN + "You come to a bridge, it looks wobbly,"
        "do you want to cross or do you want to head back? (cross/back) " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs back then
    if answer == "back":
        answer = input(
            Fore.GREEN + "You go back to the main road."
            "Now you can decide to drive forward or turn left. (forward/left) "
            + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "forward":
        game_over(
            Fore.RED +
            "You drive forward and crashed into a tree and die.\U0001F480 ")
    # if users inputs left then
    if answer == "left":
        chapter_lake()
    # if user inputs cross then
    elif answer == "cross":
        chapter_stranger()
    else:
        print(Fore.RED + "Not a valid answer. You die. \U0001F480 ")
        game_over()


def chapter_stranger():
    answer = input(
        Fore.GREEN +
        "You crossed the bridge and meet a stranger, do you want to talk to them? (y/n) "
        + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "n":
        game_over(
            Fore.RED +
            "The stranger was not pleased by you and murdered you. \U0001F480")
    elif answer == "y":
        answer = input(Fore.GREEN +
            "You talk to a wizard and they ask you,"
            "do you want to be a wizard? (y/n) " + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "y":
            game_over(Fore.RED +
                      "You are a wizard and you WIN the game! \U0001f3c6",
                      win=True)
        elif answer == "n":
            game_over(
                Fore.RED +
                "The stranger was not pleased by you and murdered you. \U0001F480"
            )


def chapter_lake():
    answer = input(Fore.GREEN + "You come to a lake,"
                   "do you want to swim or go back? (swim/back) " +
                   Fore.LIGHTMAGENTA_EX).lower()
    if answer == "swim":
        game_over(
            Fore.RED +
            "You swam across the lake and were eaten by a shark. \U0001F480 ")

    elif answer == "back":
        answer = input(
            Fore.GREEN + "You go to the main road."
            "Now you can decide to drive forward or turn left. (forward/left) "
            + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "forward":
            chapter_tree()
        elif answer == "left":
            game_over(Fore.RED + "You died. \U0001F480")
    else:
        game_over(Fore.RED + "Not a valid answer. You die.")


def chapter_mountain():
    answer = input(Fore.GREEN + "\nYou reached a mountain \U000026F0. \n"
                                "Do you want to climb or go back? (Type \"climb/c\" to proceed or "
                                "\"back/b\" to return) : " +
                   Fore.LIGHTMAGENTA_EX).lower()
    if answer == "climb" or answer == 'c':
        game_over(
            Fore.RED +
            "You climbed to the peak \nbut due to low temperature you frozen. \U0001F976 ")

    elif answer == "back" or answer == 'b':
        answer = input(
            Fore.GREEN + "You return to the main road."
                         "Now you can choose to drive straight ahead or turn left. (Type \"forward/f\" to proceed or "
                         "\"left/l\" to return.) : "
            + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "forward" or answer == 'f':
            chapter_tree()
        elif answer == "left" or answer == 'l':
            game_over(Fore.RED + "You died. \U0001F480")
    else:
        game_over(Fore.RED + "I'm sorry, I don't understand the input. You Died. \U0001F480")


def chapter_tree():
    answer = input(
        Fore.GREEN +
        "You are very hungry and you see a tree with apples, do you want to eat the fruit? (y/n) "
        + Fore.LIGHTMAGENTA_EX)
    if answer == "y":
        game_over(
            Fore.RED +
            "You ate the fruit but it was poisonous and you died. \U0001F480")
    elif answer == "n":
        answer = input(Fore.GREEN + 
            "You are nearly starving to death. Do you want to eat Pears instead of apples? (y/n) "
            + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "y":
            game_over(
                Fore.RED +
                "You ate the pears but they were poisonous and you died. \U0001F480"
            )
        elif answer == "n":
            game_over(
                Fore.RED +
                "You were so hungry that you were nearly going to die in a few seconds, but a lovely gentleman gave you some food and you WIN the game! \U0001f3c6",
                win=True,
            )

        else:
            print(Fore.RED + "Not a valid answer. You die. \U0001F480")
            game_over()


def game_over(message: str = None, *, end_game=True, win=False):
    "Prints Game over message"
    if message:
        print(message)
    if win:
        print("CONGRATULATIONS on winning the game!")
    else:
        print(Fore.BLUE + "Game over")
        print(Fore.LIGHTYELLOW_EX + "Thanks for playing!")
    if game_over:
        # Play Again
        answer = input(Fore.YELLOW + "Do you want to play again? (y/n) " +
                       Fore.LIGHTBLUE_EX)
        if answer == "y" or answer == "yes":
            random.choice(my_list)()
        if music == "on":
            print(Fore.GREEN + "Music is on")
        elif music == "off":
            print(Fore.RED + "Music is off")
            music.music()
        else:
            print(Fore.RED + "Thanks for playing!")
            musicTimer.musicTimerObj.cancel()  # stop music thread
            # make sure to call these 2 lines every time program exits
            musicTimer.musicTimerObj.join()

            exit()


my_list = [chapter_bridge, chapter_lake, chapter_mountain]
