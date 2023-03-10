def music():
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("Music/sotb.mp3")
    sound.play()
