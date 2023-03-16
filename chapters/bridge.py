from chapters.lake import *
from chapters.stranger import *
from GUI.GUI import *
from chapters import *

def chapter_bridge():
    if GUIInstance.ask_question("You come to a bridge, it looks wobbly. Do you want to cross it or do you want to head back?", "Cross", "Back"):
        # 1. Cross
        chapter_stranger()
    
    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            game_over("You drive forward and crash into a tree and die.\U0001F480")
        else:
            # 2. Left
            chapter_lake()