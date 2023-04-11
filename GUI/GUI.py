from GUI.GUIObjects import Button, TextBox, Toggle
import music.musicTimer as musicTimer  # stop music thread in this file
import chapters
import sys

from colorama import Fore
import random

import pygame
pygame.init()

class GUI:
    def __init__(self):
        self.bg_color = (128, 255, 0)
        self.space_between_text = 60
        self.music_toggle_size = 88


    def set_params_no_gui(self):
        self.run_gui = False

    def set_params(self, screen_width: int, screen_height: int, screen: pygame.Surface):
        self.run_gui = True

        # find a font that can draw emojis
        fonts = pygame.sysfont.get_fonts()
        if emojis := [font for font in fonts if "emoji" in font]:
            self.font = pygame.font.SysFont(emojis[0], 60)
            self.button_font = pygame.font.SysFont(emojis[0], 40)
            self.small_font = pygame.font.SysFont(emojis[0], 30)

        else:
            print("Didn't find font with emojis")

            self.font = pygame.font.Font(None, 60)
            self.button_font = pygame.font.Font(None, 40)
            self.small_font = pygame.font.Font(None, 30)
        self.button_left = Button(screen_width * .25, screen_height * .9, 200, 60, text="LEFT", font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
        self.button_right = Button(screen_width * .75, screen_height * .9, 200, 60, text="RIGHT", font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
        self.buttons_lst = [self.button_left, self.button_right]
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        # Logo
        logo_width = 400

        self.logo = pygame.image.load("assets/images/logo.png")
        aspect_ratio = self.logo.get_size()[1] / self.logo.get_size()[0]
        self.logo = pygame.transform.smoothscale(self.logo, (logo_width, logo_width * aspect_ratio))

        # BG
        bg_height = self.screen_height
        self.background = pygame.transform.smoothscale(pygame.image.load("assets/images/landscape.png"), (bg_height* 1.778, bg_height))


    # private function
    def __seperate_text_to_rows(self, text: str, max_width: int, font_to_use: pygame.font.Font) -> list:
        """Takes in: text to split\n max_width allowed, example: screen width\n font to use: What font will the text be rendered in \n
        RETURNS pygame.Surface renders of the text that are split according to max_width"""

        output_text_objs = []
        words = text.split(" ")

        # The index of 'words' where the text was longer than 'max_width'
        last_overflow_index = 0

        _index_in_words = 0
        # every loop add 1 more word to sentece
        while _index_in_words < len(words) + 1:
            _index_in_words += 1

            # get words that are up to current '_index_in_words'
            _text = words[last_overflow_index : _index_in_words]
            _text_render = font_to_use.render(" ".join(_text), True, (0,0,0))


            # if the render is wider than allowed, render the things that fit in
            if _text_render.get_size()[0] > max_width:
                _out_text = " ".join(words[last_overflow_index : _index_in_words - 1])
                _final_text = font_to_use.render(_out_text, True, (0,0,0))
                output_text_objs.append(_final_text)

                last_overflow_index = _index_in_words - 1
                _index_in_words -= 1

            # if last word, add rest and break from loop
            if _index_in_words == len(words):
                _out_text = " ".join(words[last_overflow_index : _index_in_words])
                _final_text = font_to_use.render(_out_text, True, (0,0,0))
                output_text_objs.append(_final_text)
                break


        return output_text_objs

    # private function
    def __render_text_center(self, texts: list):
        """Render list of pygame text renders in the center of the screen"""
        # Get total height of text elements rendered. Sum all text heights and add the spaces between them
        total_height = sum(
            x.get_size()[1] for x in texts
        ) + self.space_between_text * (len(texts) - 1)

        # Loop through every text element and render it
        for _i, _text in enumerate(texts):
            _text_width, _text_height = _text.get_size()

            # Get the position to render it in the center of screen
            center_x = self.screen_width / 2 - _text_width / 2
            center_y = (self.screen_height / 2 - _text_height / 2 + 60 * _i) - total_height / 4 # make all texts centered

            self.screen.blit(_text, (center_x, center_y))


    def ask_question(self, question: str, left_btn_txt: str, right_btn_txt: str) -> bool:
        """Ask a question with two answers.\n
            RETURNS: If pressed left_button: Return True. If pressed right_button: Return False"""
        if not self.run_gui:
            return self.__ask_question_no_gui(
                f"{question} ({left_btn_txt} / {right_btn_txt}) ",
                left_btn_txt,
                right_btn_txt,
                color_before=Fore.GREEN,
                color_after=Fore.LIGHTMAGENTA_EX,
            )

        # Initalize texts and buttons
        text_renders = self.__seperate_text_to_rows(question, self.screen_width - 50, self.font)
        self.button_left.text = left_btn_txt
        self.button_right.text = right_btn_txt

        # Basic pygame window loop
        while True:
            self.screen.blit(self.background, (0, 0))

            # Update buttons
            for btn in self.buttons_lst:
                btn.draw(self.screen)
                btn.check_hover(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                # If left mousebutton clicked, check if clicked on a button
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0]
                ):
                    if self.button_left.check_click():
                        return True
                    if self.button_right.check_click():
                        return False

            # Render the text
            self.__render_text_center(text_renders)
            pygame.display.update()


    def text_until_enter(self, text: str):
        """Render text in the center of the screen until enter is pressed.\n
            Includes a small text that says 'press enter to continue'"""

        # initialize texts
        text_renders = self.__seperate_text_to_rows(text, self.screen_width - 50, self.font)
        enter_text = self.small_font.render("Press Enter to continue", True, (255,255,255))

        while True:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                # Return when enter pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            # Render the center text
            self.__render_text_center(text_renders)

            # Render 'press enter to continue' text
            self.screen.blit(enter_text, (self.screen_width / 2 - enter_text.get_size()[0] / 2, 
                                          self.screen_height * .9  - enter_text.get_size()[1] / 2))
            pygame.display.update()


    def exit_func(self):
        musicTimer.musicTimerObj.cancel()  # stop music thread, make sure to call these 2 lines every time program exits
        musicTimer.musicTimerObj.join()
        sys.exit(1)

    def start_screen(self):
        if not self.run_gui: 
            self.__start_screen_no_gui()
            return

        text_box_w = 300
        text_box_h = 100
        name_text_box = TextBox((self.screen_width / 2 - text_box_w / 2, 
                                self.screen_height * .7 - text_box_h / 2, text_box_w, text_box_h), font=self.font)    

        music_toggle = Toggle(self.screen_width - self.music_toggle_size - 20, 20, "assets/images/MusicOn.png", "assets/images/MusicOff.png", (self.music_toggle_size, self.music_toggle_size))
        
        text = self.font.render("Hi! What is you name?", True, (255, 255, 255))

        got_name = False

        while not got_name:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.logo, (self.screen_width / 2 - self.logo.get_size()[0] / 2, 
                                        self.screen_height * .3 - self.logo.get_size()[1] / 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                name_text_box.get_event(event)
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0]
                ):
                    music_toggle.check_click(pygame.mouse.get_pos())

                    if music_toggle.get_state() == 1:
                        pygame.mixer.unpause()
                    else:
                        pygame.mixer.pause()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    player_name = "".join(name_text_box.buffer)
                    got_name = True

            self.screen.blit(text, (self.screen_width / 2 - text.get_size()[0] / 2, 
                                    self.screen_height * .85))
            music_toggle.draw(self.screen)

            name_text_box.update()
            name_text_box.draw(self.screen)
            pygame.display.update()

        self.text_until_enter(f"Welcome {player_name} to this adventure!")

    def __ask_question_no_gui(self, question: str, first: str, second: str, color_before: Fore=None, color_after: Fore=None) -> bool:
        while True:
            q = ""

            if color_before:
                q += color_before

            q += question

            if color_after:
                q += color_after

            answer = input(q)
            if answer.lower() == first.lower():
                return True
            if answer.lower() == second.lower():
                return False

            print("Invalid answer, try again.")

    def __start_screen_no_gui(self):
        name = input(f"{Fore.YELLOW}Type your name: {Fore.LIGHTBLUE_EX}")
        print(f"{Fore.LIGHTGREEN_EX}Welcome", name, "to this adventure!")

        if self.__ask_question_no_gui("Do you want to play? (yes / no) ", "yes", "no", color_before=Fore.YELLOW, color_after=Fore.LIGHTBLUE_EX):
            # Yes
            print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
        else:
            # No
            print("See you later! \U0001F600")
            self.exit_func()

        random.choice(chapters.my_list)()
        # if self.__ask_question_no_gui("Do you want music? \U0001F3B5 (yes / no) ", "yes", "no", color_before=Fore.YELLOW, color_after=Fore.LIGHTBLUE_EX):
        #     # Yes
        #     music_player.music()
        #     random.choice(chapters.my_list)()
        # else:
        #     # No
        #     print(Fore.LIGHTGREEN_EX + "Okay \U0001F600")

# Use this object when calling any function from GUI class
GUIInstance = GUI()
