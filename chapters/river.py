from GUI.GUI import GUIInstance
from chapters import *

def chapter_river():
    if GUIInstance.ask_question("You come to a river, you can walk around it or swim across.", "Walk", "Swim"):
        # 1. Walk
        if GUIInstance.ask_question("You walked for many miles, ran out of water and remembered that there was a shop far away which supplies water. Do you want to go there?", "Yes", "No"):
            # 2. Yes
            if GUIInstance.ask_question("You went 10 miles walking and bought 10 liters of drinking water. Do you want to drink the water?", "Yes", "No"):
                # 3. Yes
                GUIInstance.text_until_enter("You drank 5 liters of water and now you feel refreshed.")
                if GUIInstance.ask_question("Do you want to walk further or go back home?", "Further", "Home"):
                    # 4. Further
                    game_over("You walked 100 more miles and you WIN the game! \U0001f3c6", win=True)
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