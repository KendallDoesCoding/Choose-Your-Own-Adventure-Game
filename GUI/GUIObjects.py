import pygame, os
pygame.init()

class Button:
    def __init__(self, x, y, width, height, bg_color=(120,120,120), hover_color=(150,150,150), text="Text", text_color=(0,0,0), font_size=18, center_text = True, border=0, border_color=(0,0,0), font=None):
        self.x = x - width / 2
        self.y = y - height / 2
        self.width = width
        self.height = height
        self.pos = (self.x, self.y)
        self.size = (width,height)
        self.image = pygame.Surface(self.size)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.hovering = False
        
        if font is None:
            self.font = pygame.font.Font(None, font_size)
        else: 
            self.font = font

        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.center_text = center_text
        self.border = border
        self.border_color = border_color


    def draw(self, screen):
        if self.hovering:
            if self.border == 0:
                self.image.fill(self.hover_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.hover_color, (self.border, self.border, self.width-self.border*2, self.height-self.border*2))

        else:
            if self.border == 0:
                self.image.fill(self.bg_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.bg_color, (self.border, self.border, self.width-self.border*2, self.height-self.border*2))

        #text        
        text = self.font.render(self.text, True, self.text_color)
        text_width = text.get_width()
        text_height = text.get_height()

        if self.center_text:
            self.image.blit(text, (self.width//2-text_width//2,self.height//2-text_height//2))
        else: self.image.blit(text, (self.border+5,self.height//2-text_height//2))
        screen.blit(self.image, self.pos)


    def check_hover(self, mouse_pos):
        if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x+self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y+self.height:
            self.hovering = True
        else:
            self.hovering = False


    def check_click(self):
        if self.hovering:
            return True
            
        return False
    

class Text_box():
    def __init__(self,x,y,width,height,bg_color=(155,155,155),active_color=(200,200,200),
                text_size=24, text_color=(0,0,0), border=0, border_color=(0,0,0), only_letters=False,
                only_numbers=False, placeholder_txt="Text", placeholder_color=(100,100,100), max_chars=-1):
        self.x = x - width / 2
        self.y = y - height / 2
        self.width = width
        self.height = height 
        self.pos = (self.x, self.y)
        self.size = (width, height)
        self.image = pygame.Surface((width, height))
        self.bg_color = bg_color
        self.active_color = active_color
        self.active = False
        self.text = ""
        self.text_size = text_size
        self.text_color = text_color
        self.border_color = border_color
        self.font = pygame.font.Font(None, self.text_size)
        self.border = border
        self.numbers = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        self.only_letters = only_letters
        self.only_numbers = only_numbers
        self.placeholder_txt = placeholder_txt
        self.placeholder_color = placeholder_color
        self.max_chars = max_chars # -1 is infinite
        if self.max_chars < 0:
            self.inifnite_chars = True
        else: self.inifnite_chars = False

    def draw(self, screen):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.bg_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.bg_color, (self.border, self.border, 
                                 self.width-self.border*2, self.height-self.border*2))

        else:
            if self.border == 0:
                self.image.fill(self.active_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.active_color, (self.border, self.border, 
                                 self.width-self.border*2, self.height-self.border*2))

        #rendering text
        if self.text == "":
            placeholder_txt = self.font.render(self.placeholder_txt, True, self.placeholder_color)
            placeholder_txt.set_alpha(100)
            text_width = placeholder_txt.get_width()
            text_height = placeholder_txt.get_height()
            if text_width < self.width-self.border*2:
                self.image.blit(placeholder_txt, (2+self.border*2,(self.height-text_height)//2))
            else:
                self.image.blit(placeholder_txt, ((self.border*2)+(self.width-text_width-self.border*3),(self.height-text_height)//2))

        else:
            text = self.font.render(self.text, False, self.text_color)
            text_width = text.get_width()
            text_height = text.get_height()
            if text_width < self.width-self.border*2:
                self.image.blit(text, (2+self.border*2,(self.height-text_height)//2))
            else:
                self.image.blit(text, ((self.border*2)+(self.width-text_width-self.border*3),(self.height-text_height)//2))

        screen.blit(self.image, self.pos)
    
    def add_text(self, key):
        
        if not self.active:
            return

        try:
            # Backspace    
            if key == 8:
                text = list(self.text)
                text.pop()
                self.text = "".join(text)

            if len(self.text) < self.max_chars or self.inifnite_chars:
                # Adding numbers
                if not self.only_letters:
                    if key in self.numbers:
                        text = list(self.text)
                        if key < 100:
                            text.append(str(key-48))
                        self.text = "".join(text)
                
                # Spacebar
                if key == 32:
                    text = list(self.text)
                    text.append(" ")
                    self.text = "".join(text)
                # Dot
                elif key == 46:
                    text = list(self.text)
                    text.append(".")
                    self.text = "".join(text)
                

                # Add letters
                if not self.only_numbers:
                    if chr(key).isalpha():
                        text = list(self.text)
                        text.append(chr(key))
                        self.text = "".join(text)
                    # Coma
                    elif key == 44:
                        text = list(self.text)
                        text.append(",")
                        self.text = "".join(text)
        except:
            # Invalid key
            print(key, "is invalid key")

    def check_click(self, mouse_pos):
        if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x+self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y+self.height:
            self.active = True
        else:
            self.active = False

    def return_val(self):
        if self.only_letters:
            return self.text

        try:
            return float(self.text)
        except:
            return 0
        

class Toggle:
    def __init__(self, x: int, y: int, image_on_path: str, image_off_path: str, image_size: tuple, default_state: int=1):
        self.x = x
        self.y = y
        self.w, self.h = image_size
        self.image_on = pygame.transform.smoothscale(pygame.image.load(image_on_path), image_size)
        self.image_off = pygame.transform.smoothscale(pygame.image.load(image_off_path), image_size)
        self.default_state = default_state
        self.current_state = 1 # 1 on, -1 off

    def check_click(self, mouse_pos: tuple):
        if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x+self.w and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y+self.h:
            self.current_state *= -1
        
    def draw(self, screen: pygame.Surface):
        if self.current_state == 1:
            screen.blit(self.image_on, (self.x, self.y))
        elif self.current_state == -1:
            screen.blit(self.image_off, (self.x, self.y))

    def get_state(self) -> int:
        return self.current_state

# Taken from https://github.com/Mekire/pygame-textbox 
import string
import pygame as pg

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

class TextBox(object):
    def __init__(self,rect,**kwargs):
        self.rect = pg.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.blink = True
        self.blink_timer = 0.0
        self.process_kwargs(kwargs)

    def process_kwargs(self,kwargs):
        defaults = {"id" : None,
                    "command" : None,
                    "active" : True,
                    "color" : pg.Color("white"),
                    "font_color" : pg.Color("black"),
                    "outline_color" : pg.Color("black"),
                    "outline_width" : 2,
                    "active_color" : pg.Color("black"),
                    "font" : pg.font.Font(None, self.rect.height+4),
                    "clear_on_enter" : False,
                    "inactive_on_enter" : True,
                    "max_length" : 999}
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("InputBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)

    def get_event(self,event):
        if event.type == pg.KEYDOWN and self.active:
            if event.key in (pg.K_RETURN,pg.K_KP_ENTER):
                self.execute()
            elif event.key == pg.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.unicode in ACCEPTED:
                if len(self.buffer) < self.max_length:
                    self.buffer.append(event.unicode)

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)

    def execute(self):
        if self.command:
            self.command(self.id,self.final)
        self.active = not self.inactive_on_enter
        if self.clear_on_enter:
            self.buffer = []

    def update(self):
        new = "".join(self.buffer)
        if new != self.final:
            self.final = new
            self.rendered = self.font.render(self.final, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x+2,
                                                      centery=self.rect.centery)
            if self.render_rect.width > self.rect.width-6:
                offset = self.render_rect.width-(self.rect.width-6)
                self.render_area = pg.Rect(offset,0,self.rect.width-6,
                                           self.render_rect.height)
            else:
                self.render_area = self.rendered.get_rect(topleft=(0,0))
        if pg.time.get_ticks()-self.blink_timer > 200:
            self.blink = not self.blink
            self.blink_timer = pg.time.get_ticks()

    def draw(self,surface):
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width*2,self.outline_width*2)
        surface.fill(outline_color,outline)
        surface.fill(self.color,self.rect)
        if self.rendered:
            surface.blit(self.rendered,self.render_rect,self.render_area)
        if self.blink and self.active:
            curse = self.render_area.copy()
            curse.topleft = self.render_rect.topleft
            surface.fill(self.font_color,(curse.right+1,curse.y,2,curse.h))
