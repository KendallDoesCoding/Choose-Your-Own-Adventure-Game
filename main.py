from chapters import *

def game_over(message: str = None, *, end_game=True, win=False):
    "Prints Game over message"
    if message:
        print(message)
    if win:
        print("CONRATULATIONS on winning the game!")
    else:
        print("Game over")
    print("Thanks for playing!")
    if end_game:
        exit()

def main():
    # welcome to the game
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    # do you want to play?
    answer = input("Do you want to play? (y/n) ")
    if answer == "y" or answer == "yes":
        # starting the game
        print("Let's play!")
        # start the game
        # q1
        answer = input(
            "You are on a dirt road. Which way to you want to go left or right? "
        ).lower()
        # if user inputs left then
    if answer == "left":
        chapter_river()

    # if user inputs right then
    if answer == "right":
        chapter_bridge()

    if answer == "n" or answer == "no":
        print("See you later!")
        exit()


if __name__ == "__main__":
    main()
