from GUI.GUI import *
from chapters import *

def chapter_stranger():
    if GUIInstance.ask_question("You cross the bridge and meet a stranger, do you talk to them?", "Yes", "No"):
        # 1. Yes
        if GUIInstance.ask_question("You talk a wizard and he asks you, do you want to be a wizard?", "Yes", "No"):
            # 2. Yes
            game_over("You bacome a wizard and WIN the game! \U0001f3c6", win=True)
        else:
            # 2. No
            game_over("The stranger was not pleased by you and murdered you. \U0001F480")
    else:
        # 1. No
        game_over("The stranger was not pleased by you and murdered you. \U0001F480")