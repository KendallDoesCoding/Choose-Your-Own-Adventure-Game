import random

# import the colorama module
import colorama
from colorama import Fore

from music_player import *
from GUI.GUI import GUIInstance

#Initialize Chapters
from chapters.river import *
from chapters.lake import *
from chapters.mountain import *
from chapters.bridge import *


colorama.init(convert=True)

# start the game

# NOT CALLED ANYWHERE
def start():
    if GUIInstance.ask_question("You are on a dirt road. Which way do you want to go left or right?", "Left", "Right"):
        random.choice(my_list)()
    else:
        random.choice(my_list)()



my_list = [chapter_bridge, chapter_lake, chapter_mountain, chapter_river]
