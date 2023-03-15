from GUI.GUIObjects import Button, TextBox
import music.musicTimer as musicTimer  # stop music thread in this file

import pygame
pygame.init()

class GUI:
    def __init__(self):
        self.bg_color = (128, 255, 0)
        self.space_between_text = 60

        # Logo
        logo_width = 400

        self.logo = pygame.image.load("assets/images/logo.png")
        aspect_ratio = self.logo.get_size()[1] / self.logo.get_size()[0]
        self.logo = pygame.transform.smoothscale(self.logo, (logo_width, logo_width * aspect_ratio))

        # find a font that can draw emojis
        fonts = pygame.sysfont.get_fonts()
        emojis = [font for font in fonts if "emoji" in font]

        if emojis == []:
            print("Didn't find font with emojis")

            self.font = pygame.font.Font(None, 60)
            self.button_font = pygame.font.Font(None, 40)
            self.small_font = pygame.font.Font(None, 30)
        else:
            self.font = pygame.font.SysFont(emojis[0], 60)
            self.button_font = pygame.font.SysFont(emojis[0], 40)
            self.small_font = pygame.font.SysFont(emojis[0], 30)


    def set_params(self, screen_width: int, screen_height: int, screen: pygame.Surface):
        self.button_left = Button(screen_width * .25, screen_height * .9, 200, 60, text="LEFT", font=self.button_font, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
        self.button_right = Button(screen_width * .75, screen_height * .9, 200, 60, text="RIGHT", font=self.button_font, bg_color=(200, 200, 200), hover_color=(220, 220, 220))
        self.buttons_lst = [self.button_left, self.button_right]
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()
        

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
        total_height = sum([x.get_size()[1] for x in texts]) + self.space_between_text * (len(texts) - 1)
        
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
        
        # Initalize texts and buttons
        text_renders = self.__seperate_text_to_rows(question, self.screen_width - 50, self.font)
        self.button_left.text = left_btn_txt
        self.button_right.text = right_btn_txt
        
        # Basic pygame window loop
        while(True):
            self.screen.fill(self.bg_color)

            # Update buttons
            for btn in self.buttons_lst:
                btn.draw(self.screen)
                btn.check_hover(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()
                
                # If left mousebutton clicked, check if clicked on a button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
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
        enter_text = self.small_font.render("Press Enter to continue", True, (0,0,0))

        while(True):
            self.screen.fill(self.bg_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()
                
                # Return when enter pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
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
        exit()

    def start_screen(self):
        text_box_w = 300
        text_box_h = 100
        name_text_box = TextBox((self.screen_width / 2 - text_box_w / 2, 
                                self.screen_height * .7 - text_box_h / 2, text_box_w, text_box_h), font=self.font)    
        
        text = self.font.render("Hi! What is you name?", True, (0,0,0))

        got_name = False

        while (not got_name):
            self.screen.fill(self.bg_color)
            self.screen.blit(self.logo, (self.screen_width / 2 - self.logo.get_size()[0] / 2, 
                                         self.screen_height * .3 - self.logo.get_size()[1] / 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()
                
                name_text_box.get_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player_name = "".join(name_text_box.buffer)
                        got_name = True
            
            self.screen.blit(text, (self.screen_width / 2 - text.get_size()[0] / 2, 
                                    self.screen_height * .85))
            name_text_box.update()
            name_text_box.draw(self.screen)
            pygame.display.update()

        self.text_until_enter(f"Welcome {player_name} to this adventure!")

# Use this object when calling any function from GUI class
GUIInstance = GUI()