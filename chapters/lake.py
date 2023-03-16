from GUI.GUI import *
from chapters import *
from chapters.tree import *

def chapter_lake():
    if GUIInstance.ask_question("You turned left and you come to a lake, do you want to swim or go back?", "Swim", "Back"):
        # 1. Swim
        game_over("You swam across the lake and were eaten by a shark. \U0001F480 ")
    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            game_over("You died. \U0001F480") # Swapped these two answers around because there is a same question with different answer 
        else:
            # 2. Left
            chapter_tree()