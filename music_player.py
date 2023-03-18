import os
import random
import threading

import colorama
from colorama import Fore

import music.musicTimer as musicTimer
from GUI.GUI import GUIInstance

# Initialize songs


def fluffingaduck(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/Fluffing-A-Duck.mp3")
    sound.set_volume(0.5)  # Now plays at 50% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED +
              "Currently Playing - Fluffing a Duck by Kevin Macleod")

    return sound


def snakeonthebeach(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/sotb.mp3")
    sound.set_volume(0.2)  # Now plays at 20% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Snake On The Beach by Nico Staf")

    return sound


def aparisiancafe(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/A Parisian Cafe.mp3")
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - A Parisian Cafe by Aaron Kenny")

    return sound


def bliss(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/bliss.mp3")
    sound.set_volume(0.9)  # Now plays at 90% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Bliss by Luke Bergs")

    return sound


def happynjoyfulchildren(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/happyandjoyfulchildren.mp3")
    sound.set_volume(0.9)  # Now plays at 90% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Happy and Joyful Children")

    return sound


def tropicalsoul(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/tropicalsoul.mp3")
    sound.set_volume(0.9)  # Now plays at 90% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Tropical Soul by Luke Bergs")

    return sound


def newlands(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/newlands.mp3")
    sound.set_volume(0.5)  # Now plays at 50% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - New Lands by Alex-Productions")

    return sound


def beachvibes(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/beachvibes.mp3")
    sound.set_volume(0.5)  # Now plays at 50% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Beach Vibes by Luke Bergs")

    return sound

def tropicalfever(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/tropicalfever.mp3")
    sound.set_volume(0.2)  # Now plays at 20% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Tropical Fever by Luke Bergs & LiQWYD")

    return 

def happyadricanvillage(print_song_name=True):
    import os

    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/happyafricanvillage.mp3")
    sound.set_volume(0.2)  # Now plays at 20% of full volume.
    sound.play()

    if print_song_name:
        print(Fore.RED + "Currently Playing - Happy African Village by John Bartmann")

    return sound



songs = [
    fluffingaduck,
    snakeonthebeach,
    aparisiancafe,
    bliss,
    happynjoyfulchildren,
    tropicalsoul,
    newlands,
    beachvibes,
    tropicalfever,
    happyadricanvillage
]


def music():
    import pygame

    pygame.init()
    pygame.mixer.init()

    start_song(print_song_name = not GUIInstance.run_gui)
    if not GUIInstance.run_gui:
        print(Fore.BLUE + "Music has started")


# Another function to not print all the stuff when starting new song
def start_song(print_song_name=True):
    sound = random.choice(songs)(print_song_name)

    # create a Timer object that will run this function again after the song has ended
    musicTimer.musicTimerObj = threading.Timer(
        sound.get_length(), start_song, kwargs={"print_song_name": False})
    musicTimer.musicTimerObj.start()


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
