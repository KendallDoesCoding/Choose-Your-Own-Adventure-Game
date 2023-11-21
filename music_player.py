import os
import random
import threading
from colorama import Fore
import pygame
import music.musicTimer as musicTimer
from GUI.GUI import GUIInstance


class Song:
    def __init__(self, mp3_filename, title, volume=0.5):
        self.mp3_filename = f"Music/{mp3_filename}"
        self.volume = volume
        self.title = title

    def play(self):
        sound = pygame.mixer.Sound(f"{self.mp3_filename}")
        sound.set_volume(self.volume)  # Now plays at 50% of full volume.
        sound.play()
        return sound


songs = [
    Song("fluffing_a_duck.mp3", "Fluffing a Duck by Kevin Macleod"),
    Song("sotb.mp3", "Snake On The Beach by Nico Staf", 0.2),
    Song("parisian_cafe.mp3", "A Parisian Cafe by Aaron Kenny"),
    Song("bliss.mp3", "Bliss by Luke Bergs", 0.9),
    Song("happyandjoyfulchildren.mp3", "Happy and Joyful Children", 0.9),
    Song("tropicalsoul.mp3", "Tropical Soul by Luke Bergs", 0.9),
    Song("newlands.mp3", "New Lands by Alex-Productions"),
    Song("beachvibes.mp3", "Beach Vibes by Luke Bergs"),
    Song("tropicalfever.mp3", "Tropical Fever by Luke Bergs & LiQWYD"),
    Song("happyafricanvillage.mp3", "Happy African Village by John Bartmann", 0.2),
]


def music():
    pygame.init()
    pygame.mixer.init()
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    start_song(print_song_name=not GUIInstance.run_gui)
    if not GUIInstance.run_gui:
        print(f"{Fore.BLUE} Music has started")


def start_song(print_song_name=True):
    song = random.choice(songs)
    channel = song.play()
    if print_song_name:
        print(Fore.RED + f"Currently Playing - {song.title}")
    # create a Timer object that will run this function again after the song has ended
    musicTimer.musicTimerObj = threading.Timer(
        channel.get_length(), start_song)
    musicTimer.musicTimerObj.start()
