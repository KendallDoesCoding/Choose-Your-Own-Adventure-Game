from GUI.GUI import *
from chapters import *

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
            game_over("You were super hungry and nearly died, but a lovely gentleman gave you some food and you WIN the game! \U0001f3c6", win=True)