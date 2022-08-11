# welcome to the game
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# do you want to play?
answer = input("Do you want to play? (y/n) ")
if answer == "y":
    # starting the game
    print("Let's play!")
    # start the game
    # q1
    answer=input("You are on a dirt road. Which way to you want to go left or right? " ).lower()
    # if user inputs left then
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Type walk to walk around & swim to swim across. ").lower()

    # if user inputs swim then
    if answer == "swim":
        print("You swam accross the river and were eaten by an aligator.")
        print("Game over")
        print("Thanks for playing!")
        exit()

    #if user inputs walk then
    elif answer =="walk":
    # q2
        answer = input("You walked for many miles, ran out of water and remembered that there was a shop far away (10 miles/16kms) which supplies water. Do you want to go there (yes/no)?")
    #if user inputs yes then
        if answer == "yes":
            print("You walked to the shop and bought some water.")
    #q3
        answer = input("You are thirsty, do you want to drink some water (yes/no)?")
    #if user inputs yes then
        if answer == "yes":
                print("You went 10 miles walking and bought 10 liters of drinking water")
    #q4
        answer = input("You drank 5 liters of water and now you feel refreshed. Do you want to walk further or go back home? (further/home)")
    #if user inputs further then
        if answer == "further":
                print("You walked 100 more miles and you WIN the game!")
                print("Thanks for playing!")
                print("CONRATULATIONS ON WINNING THE GAME!")
                exit()
    #if user inputs home then
        if answer == "home":
                print("You fell down, went to hospital, and died.")
                print("Game over")
                print("Thanks for playing!")
                exit()
    #if user doesn't want to walk 10miles to buy water and inputs no then
        elif answer=="no":
            print("You fell sick, went to hospital, and died.")
            print("Game over")
            print("Thanks for playing!")
            exit()
    # if user doesn't input left or right then
    else:
        print('Not a valid answer. You die.')
    print("Game over")
    print("Thanks for playing!")
    exit()

# if user inputs right then
if answer == "right":
        answer = input("You come to a bridge, it looks wobbly, do you want it or do you want to head back? (cross/back)")
        # if user inputs back then
        if answer == "back":
                answer = input ("You go back to the main road. Now you can decide to drive forward or turn left. (forward/left)")
        if answer =="forward":
            answer = input("You drive forward and crash into a tree and die.")
            print("Game over")
            print("Thanks for playing!")
            exit()
        # if users inputs left then
        if answer == "left":
            answer = input("You turned left and you come to a lake, do you want to swim or go back? (swim/back)")
            if answer == "swim":
                answer = input ("You swam accross the lake and were eaten by a shark.")
                print("Game over")
                exit()
        
            elif answer == "back":
                answer = input("You go back to the main road. Now you can decide to drive forward or turn left. (forward/left")
                if answer == "forward":
                    answer = input("You drive forward and crash into a tree and die.")
                    print("Game over")
                    print("Thanks for playing!")
                    exit()
                elif answer == "left":
                    print("Game over")
                    print("Thanks for playing!")
                    exit()
        # user input cross then
        elif answer =="cross":
                answer = input("You cross the bridge and meet a stranger, do you talk to them? (y/n)")
                if answer == "y":
                    answer= input("You talk to the stranger and they say they are a wizard, do you want to be a wizard? (y/n)")
                    if answer == "y":
                        print("You are a wizard and you WIN the game!")
                        print("Thanks for playing!")
                        print("CONRATULATIONS ON WINNING THE GAME!")
                        exit()
                    elif answer == "n":
                        print("The stranger lied to you, and instead of making you a wizard gave you posion and you died.")
                        print("Game over")
                        print("Thanks for playing!")
                        exit()

                elif answer == "n":
                    answer = input("The stranger is a bad person and you die.")
                    print("Game over")
                    print("Thanks for playing!")
                    exit()

        else:
                print('Not a valid answer. You die.')
if answer =="n":
    print("See you later!")
    exit()