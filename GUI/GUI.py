from GUIObjects import Button

import pygame
pygame.init()


class GUI:
    def __init__(self, screen_width: int, screen_height: int):
        self.button_left = Button(screen_width * .25, screen_height * .75, 200, 40, text="LEFT", font_size=32, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
        self.button_right = Button(screen_width * .75, screen_height * .75, 200, 40, text="RIGHT", font_size=32, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
        self.buttons_lst = [self.button_left, self.button_right]