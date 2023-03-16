from GUI.GUI import *
from chapters import *

def chapter_mountain():
    if GUIInstance.ask_question("You reached a mountain. Do you want to climb it?", "Yes", "No"):
        # 1. Yes
        if GUIInstance.ask_question("You start climbing the mountain. You see a rope bridge ahead. Do you want to cross it?", "Yes", "No"):
            # 2. Yes
            game_over("You walk on the bridge, but suddenly it collapses. You fall to the ground and die \U0001F480")
        else:
            # 2. No
            if GUIInstance.ask_question("Do you want to continue climbing or go back down?", "Climb", "Back"):
                # 3. Climb
                game_over("You climb the mountain for many days, and you finally reach the top. You WIN the game! \U0001f3c6", win=True)
            else:
                # 3. Back
                GUIInstance.text_until_enter("You climb down safely.")
                random.choice(my_list)()

    else:
        # 1. No
        random.choice(my_list)()