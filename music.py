import colorama
from colorama import Fore
import random

import os


# Initialize songs
def fluffingaduck():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/Fluffing-A-Duck.mp3")
    sound.set_volume(0.5)              # Now plays at 50% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Fluffing a Duck by Kevin Macleod") 

def snakeonthebeach():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/sotb.mp3")
    sound.set_volume(0.2)              # Now plays at 20% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Snake On The Beach by Nico Staf") 


def aparisiancafe():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/A Parisian Cafe.mp3")
    sound.play()
    print(Fore.RED + "Currently Playing - A Parisian Cafe by Aaron Kenny") 

def bliss():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/bliss.mp3")
    sound.set_volume(0.9)              # Now plays at 90% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Bliss by Luke Bergs") 

def happynjoyfulchildren():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/happyandjoyfulchildren.mp3")
    sound.set_volume(0.9)              # Now plays at 90% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Happy and Joyful Children") 

def tropicalsoul():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/tropicalsoul.mp3")
    sound.set_volume(0.9)              # Now plays at 90% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Tropical Soul by Luke Bergs") 

def newlands():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/newlands.mp3")
    sound.set_volume(0.5)              # Now plays at 50% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - New Lands by Alex-Productions")

def beachvibes():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/beachvibes.mp3")
    sound.set_volume(0.5)              # Now plays at 50% of full volume.
    sound.play()
    print(Fore.RED + "Currently Playing - Beach Vibes by Luke Bergs")



songs = [fluffingaduck, snakeonthebeach, aparisiancafe, bliss, happynjoyfulchildren, tropicalsoul, newlands, beachvibes]


def music():

    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = random.choice(songs)()
    print(Fore.BLUE + "Music has started")
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"



