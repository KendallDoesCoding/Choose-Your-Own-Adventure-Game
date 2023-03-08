from colorama import Fore, Back, Style
import colorama
colorama.init(convert=True)


def start():
    answer = input(Fore.GREEN + "You are on a dirt road. Which way to you want to go left or right? " + Fore.LIGHTMAGENTA_EX).lower()
# if user inputs left then
    if answer == "left":
        chapter_river()

    # if user inputs right then
    if answer == "right":
        chapter_bridge()

def chapter_river():
    answer = input(Fore.GREEN + 
        "You come to a river, you can walk around it or swim accross."
        "Type walk to walk around & swim to swim across." + Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs swim then
    if answer == "swim":
        game_over(Fore.RED + "You swam across the river and were eaten by an aligator \U0001F480")
    # if user inputs walk then
    elif answer == "walk":
        # q2
        answer = input(Fore.GREEN + 
            "You walked for many miles, ran out of water and remembered "
            "that there was a shop far away (10 miles/16kms) which supplies water."
            "Do you want to go there (yes/no)?" + Fore.LIGHTMAGENTA_EX).lower()
            # if user inputs no then
        if answer == "no":
            game_over(Fore.RED + "You were very de-hydrated and died of thirst when you were walking. \U0001F480")
        
        # if user inputs yes then
        elif answer == "yes":
        # q3
            answer = input(Fore.GREEN +
            "You are thirsty, do you want to drink some water (yes/no)?" + Fore.LIGHTMAGENTA_EX).lower()
        # if user inputs yes then
        if answer == "yes":
            print(Fore.GREEN + 
                "You went 10 miles walking and bought 10 liters of drinking water"
            )
        # if user inputs no then
        elif answer == "no":
            game_over(Fore.RED + "You died of thirst.\U0001F480 ")
        else: 
            print(Fore.RED + "Not a valid answer. You die. \U0001F480")
            game_over()
        # q4
        answer = input(Fore.GREEN + 
            "You drank 5 liters of water and now you feel refreshed. Do you want to walk further or go back home? (further/home)" + Fore.LIGHTMAGENTA_EX).lower(
        )
        # if user inputs further then
        if answer == "further":
            game_over(Fore.BLUE + "You walked 100 more miles and you WIN the game! \U0001f3c6",
                      win=True)
        # if user inputs home then
        if answer == "home":
            game_over(Fore.RED + "A car crashed you and you were rushed to hospital. Although, it was too late by the time you reached the hospital, and you had already died. \U0001F480")
        else:
            print(Fore.RED + "Not a valid answer. You die. \U0001F480")
            game_over()
        
def chapter_bridge():
    answer = input(Fore.GREEN + "You come to a bridge, it looks wobbly,"
                   "do you want it or do you want to head back? (cross/back)" + Fore.LIGHTMAGENTA_EX).lower()
    # if user inputs back then
    if answer == "back":
        answer = input(Fore.GREEN + 
            "You go back to the main road."
            "Now you can decide to drive forward or turn left. (forward/left)" + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "forward":
        game_over(Fore.RED + "You drive forward and crash into a tree and die.\U0001F480 ")
    # if users inputs left then
    if answer == "left":
        chapter_lake()
    # if user inputs cross then
    elif answer == "cross":
        chapter_stranger()
    else:
        print(Fore.RED + "Not a valid answer. You die. \U0001F480 ")
        game_over()

def chapter_lake():
    answer = input(Fore.GREEN + "You turned left and you come to a lake,"
                   "do you want to swim or go back? (swim/back)" + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "swim":
        game_over(Fore.RED + "You swam accross the lake and were eaten by a shark. \U0001F480 ")

    elif answer == "back":
        answer = input(Fore.GREEN +
            "You go back to the main road."
            "Now you can decide to drive forward or turn left. (forward/left" + Fore.LIGHTMAGENTA_EX).lower()
        if answer == "forward":
            game_over(Fore.RED + "You drive forward and crash into a tree and die. \U0001F480")
        elif answer == "left":
            game_over(Fore.RED + "You died. \U0001F480")
    else:
        print(Fore.RED + "Not a valid answer. You die.")


def chapter_stranger():
    answer = input(Fore.GREEN +
        "You cross the bridge and meet a stranger, do you talk to them? (y/n)" + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "y":
        answer = input(Fore.GREEN +
            "You talk a wizard and they ask you,"
            "do you want to be a wizard? (y/n)")
        if answer == "y":
            game_over(Fore.RED + "You are a wizard and you WIN the game! \U0001f3c6", win=True)
    elif answer == "n":
        answer = input(Fore.RED + "The stranger was not pleased by you and murdered you. \U0001F52B")
        game_over()

def game_over(message: str = None, *, end_game=True, win=False):
    "Prints Game over message"
    if message:
        print(message)
    if win:
        print("CONRATULATIONS on winning the game!")
    else:
        print(Fore.BLUE + "Game over")
        print(Fore.LIGHTYELLOW_EX + "Thanks for playing!")
    answer = input(Fore.GREEN + "Do you want to play again? (y/n)" + Fore.LIGHTMAGENTA_EX).lower()
    if answer == "y":
        start()
    elif answer == "n":
        print(Fore.BLUE + "Thanks for playing!")
        exit()

