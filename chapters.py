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
        "You are on a dirt road \U0001F6E3. Which way do you want to go: left/l \U000021AA or right/r \U000021A9? : " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs left then
    if answer == "left" or answer == "l":
        chapter_lake()

    # if user inputs right then
    if answer == "right" or answer == "r":
        chapter_mountain()


def chapter_river():
    answer = input(
        Fore.GREEN +
        "\nYou have come across a river. You can either walk around it or swim across it.\n"
        "Type \"walk/w\" to walk around or \"swim/s\" to swim across. " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs swim then
    if answer == "swim" or answer == "s":
        game_over(
            Fore.RED +
            "You swam across the river and were eaten by an alligator \U0001F480"
        )
    # if user inputs walk then
    elif answer == "walk" or answer == "w":
        # q2
        answer = input(
            Fore.GREEN +
            "You have walked many miles and run out of water. "
            "Fortunately, there is a shop located 10 miles (16kms) away that supplies water. "
            "Would you like to go there? (yes/no): " +
            Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs no then
        if answer == "no" or answer == "n":
            game_over(
                Fore.RED +
                "You died of dehydration while walking due to severe lack of water. \U0001F480"
            )

        # if user inputs yes then
        elif answer == "yes" or answer == "y":
            print(
                Fore.GREEN +
                "You walked 10 miles and bought 10 liters of drinking water. "
            )
            # q3
            answer = input(
                Fore.GREEN +
                "You are thirsty. Would you like to drink some water? (yes/no) : " +
                Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs yes then
        if answer == "yes" or answer == "y":
            print(Fore.GREEN +
                  "After drinking 5 liters of water, you feel refreshed.")

        # if user inputs no then
        elif answer == "no" or answer == "n":
            game_over(Fore.RED + "You have died of thirst.\U0001F480 ")
        else:
            print(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480")
            random.choice(my_list)()
        # q4
        answer = input(
            Fore.GREEN +
            "You drank 5 liters of water and now you feel refreshed. \nWould you like to continue walking or return "
            "home? (Type \"continue/c\" or \"home/h\") : "
            + Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs further then
        if answer == "continue" or answer == "c":
            game_over(
                Fore.RED +
                "You walked 100 more miles and you WIN the game! \U0001f3c6",
                win=True,
            )
        # if user inputs home then
        if answer == "home" or answer == 'h':
            game_over(
                Fore.RED +
                "You were in a car crash and rushed to the hospital, but unfortunately it was too late and \nyou had "
                "already passed away by the time you arrived. \U0001F480 "
            )
        else:
            print(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480")
            game_over()


def chapter_bridge():
    answer = input(
        Fore.GREEN + "\nYou arrived at a bridge \U0001F309. It appears to be unstable. \n"
                     "Would you like to cross it or turn back? (Type \"cross/c\" to proceed or \"back/b\" to return.) "
                     ": " +
        Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs back then
    if answer == "back" or answer == "b":
        answer = input(
            Fore.GREEN + "\nYou return to the main road \U0001F6E3. Now you can choose to either continue straight "
                         "ahead or turn left.\n "
                         "(Type \"forward/f\" to proceed or \"left/l\" to return.) : "
            + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "forward" or answer == "f":
        game_over(
            Fore.RED +
            "You drive forward and crash into a tree \U0001F333, resulting in your death. \U0001F480 ")
    # if users inputs left then
    if answer == "left" or answer == "l":
        chapter_lake()
    # if user inputs cross then
    elif answer == "cross" or answer == "c":
        chapter_stranger()
    else:
        print(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480 ")
        game_over()


def chapter_stranger():
    answer = input(
        Fore.GREEN +
        "\nYou cross the bridge \U0001F309 and meet a stranger. Do you talk to them? (yes/no) : "
        + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "no" or answer == "n":
        game_over(
            Fore.RED +
            "The stranger was displeased with you and murdered you. \U0001F480")
    elif answer == "yes" or answer == "y":
        answer = input(Fore.GREEN +
                       "You encounter a wizard \U0001F9D9 who asks, "
                       "Do you want to become a wizard \U0001F9D9? (yes/no) :"
                       + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "yes" or answer == "y":
            game_over(Fore.RED +
                      "You are a wizard \U0001F9D9 and you WIN the game! \U0001f3c6",
                      win=True)
        elif answer == "no" or answer == "n":
            game_over(
                Fore.RED +
                "The stranger was displeased with you and murdered you. \U0001F480"
            )


def chapter_lake():
    answer = input(Fore.GREEN + "\nYou turn left and found a Lake \U0001F30A. \nDo you want to swim or go back? (Type "
                                "\"swim/s\" to proceed or \"back/b\" to return) : " +
                   Fore.LIGHTMAGENTA_EX).lower()
    if answer == "swim" or answer == 's':
        game_over(
            Fore.RED +
            "You swam \U0001F3CA across the Lake \U0001F30A and were eaten by a Shark \U0001F988. \U0001F923 ")

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
        game_over(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480")


def chapter_mountain():
    answer = input(Fore.GREEN + "\nYou turn right and reached a mountain \U000026F0. \n"
                                "Do you want to climb \U0001F9D7 or go back? (Type \"climb/c\" to proceed or "
                                "\"back/b\" to return) : " +
                   Fore.LIGHTMAGENTA_EX).lower()
    if answer == "climb" or answer == 'c':
        game_over(
            Fore.RED +
            "You climbed \U0001F9D7 to the peak \nbut due to low temperature \U0001F9CA you frozen. \U0001F976 ")

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
        game_over(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480")


def chapter_tree():
    answer = input(
        Fore.GREEN +
        "\nYou found an apple tree while you're starving. \nDo you want to eat the fruit? (yes/no) : "
        + Fore.LIGHTMAGENTA_EX)
    if answer == "yes" or answer == "y":
        game_over(
            Fore.RED +
            "Oops! The fruit you ate was deadly, you dead. \U0001F480")
    elif answer == "no" or answer == "n":
        answer = input(
            "You are on the verge of suffocation. \nDo you prefer to eat Pears over Apples? (yes/no) : "
            + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "yes" or answer == "y":
            game_over(
                Fore.RED +
                "Oops! The Pears were deadly, you dead. \U0001F480"
            )
        elif answer == "no" or answer == "n":
            game_over(
                Fore.RED +
                "You were so hungry that you might have passed out in a matter of seconds, \nbut a kind gentleman "
                "offered you some food, and as a result. \nyou WIN the game! \U0001f3c6",
                win=True,
            )

        else:
            print(Fore.RED + "I'm sorry, I don't understand the input. You Dead. \U0001F480")
            game_over()


def game_over(message: str = None, *, end_game=True, win=False):
    """Prints Game over message"""
    if message:
        print(message)
    if win:
        print("\nCONGRATULATIONS! You Won the game! \U0001F389")
    else:
        print(Fore.BLUE + "\nGame Over! \U0001F480")
        print(Fore.LIGHTYELLOW_EX + "Thank You \U0001F64F For Playing! ")
    if game_over:
        # Play Again
        answer = input(Fore.YELLOW + "\nLet's Play again? (yes/no) : " +
                       Fore.LIGHTBLUE_EX)
        if answer == "y" or answer == "yes":
            print("Hurray! \U0001F929 let's Play!")
            random.choice(my_list)()
        if music == "on":
            print(Fore.GREEN + "Music is on")
        elif music == "off":
            print(Fore.RED + "Music is off")
            music.music()
        else:
            print(Fore.RED + "Thank you \U0001F64F For Playing!\n")
            musicTimer.musicTimerObj.cancel()  # stop music thread
            # make sure to call these 2 line every time program exits
            musicTimer.musicTimerObj.join()

            exit()


my_list = [chapter_bridge, chapter_lake]
