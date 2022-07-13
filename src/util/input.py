
from cmath import rect
import re
import pygame
from util.text import TextEngine

class Input(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.image: pygame.Surface = pygame.Surface(self.size)
        self.rect: pygame.Rect = self.image.get_rect(center=self.pos)

        self.color: str = "#1c1c1c"
        self.alpha: int = 255
        self.border_radius = 0

        self.image.fill(self.color)
        self.image.set_alpha(self.alpha)

        self.txt_manager = TextEngine()
        self.text: str = "Input"
        self.entry_txt: str = ""
        self.placeholder: str = "Type something..."

        self.focused: bool = False
        self.hovered: bool = False

        self.set_text()
    
    def set_image(self, img: str) -> None:
        try:
            self.image = pygame.image.load(img).convert()
        except:
            raise Exception("It was not possible to change the input image. Check the path or the file extension.")
    
    def draw_bordered(self, radius: int = 50) -> None:
        '''Draws the input with rounded borders. Goes on "update" method.'''
        img_copy = self.image.copy()
        img_copy.fill("#000000")
        img_copy.set_colorkey("#000000")

        self.border_radius = radius
        pygame.draw.rect(img_copy, self.color, (0, 0, *self.rect.size), border_radius = self.border_radius)

        self.image = img_copy
        self.update_surf()
    
    def focus(self, bcolor: str = "#8f3af0", width: int = 3) -> None:
        '''Draws a border into the input if it got focus (got clicked or hovered).
        Goes on "update" method.'''
        mpos = pygame.mouse.get_pos()
        img_copy = self.image.copy()

        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(*mpos):
            self.focused = True
        elif pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(*mpos):
            self.focused = False
        
        if self.rect.collidepoint(*mpos):
            self.hovered = True
        else:
            self.hovered = False

        if self.focused or self.hovered:
            pygame.draw.rect(img_copy, bcolor, (0, 0, *self.rect.size), width, self.border_radius)
            self.image = img_copy

    def update_surf(self) -> None:
        '''Updates the input surface (self.image).'''
        # self.set_alpha(self.alpha)
        self.set_text(self.text, self.txt_manager.color)

    def set_color(self, color: str = "#1c1c1c") -> None:
        self.color = color
        self.image.fill(color)
    
    def set_alpha(self, alpha: int = 255) -> None:
        ''' Set the image alpha (transparency). The "alpha" parameter needs to be an integer ranging
        from 0 to 255.'''
        self.alpha = alpha
        self.image.set_alpha(self.alpha)
    
    def set_text(self, txt: str = "Input", color: str | tuple = "#c1c1c1") -> None:
        self.text = txt
        self.txt_manager.set_txt(self.text)
        self.txt_manager.set_color(color)
        
        img_copy = self.image.copy()
        txt_surf = self.txt_manager.render()
        img_copy.blit(txt_surf, (self.rect.width / 2 - txt_surf.get_width() / 2, self.rect.height / 2 - txt_surf.get_height() / 2))
        self.image = img_copy

    def get_input(self, key) -> None:
        '''Gets the pressed key events, handle it and convert it to text on the input.
        Goes on the event loop, under event.KEYDOWN'''
        if self.focused:
            # converts the key pressed into text inside the input
            match key:
                case pygame.K_a: self.entry_txt += "a"
                case pygame.K_b: self.entry_txt += "b"
                case pygame.K_c: self.entry_txt += "c"
                case pygame.K_d: self.entry_txt += "d"
                case pygame.K_e: self.entry_txt += "e"
                case pygame.K_f: self.entry_txt += "f"
                case pygame.K_g: self.entry_txt += "g"
                case pygame.K_h: self.entry_txt += "h"
                case pygame.K_i: self.entry_txt += "i"
                case pygame.K_j: self.entry_txt += "j"
                case pygame.K_k: self.entry_txt += "k"
                case pygame.K_l: self.entry_txt += "l"
                case pygame.K_m: self.entry_txt += "m"
                case pygame.K_n: self.entry_txt += "n"
                case pygame.K_o: self.entry_txt += "o"
                case pygame.K_p: self.entry_txt += "p"
                case pygame.K_q: self.entry_txt += "q"
                case pygame.K_r: self.entry_txt += "r"
                case pygame.K_s: self.entry_txt += "s"
                case pygame.K_t: self.entry_txt += "t"
                case pygame.K_u: self.entry_txt += "u"
                case pygame.K_v: self.entry_txt += "v"
                case pygame.K_w: self.entry_txt += "w"
                case pygame.K_x: self.entry_txt += "x"
                case pygame.K_y: self.entry_txt += "y"
                case pygame.K_z: self.entry_txt += "z"
                case pygame.K_0: self.entry_txt += "0"
                case pygame.K_1: self.entry_txt += "1"
                case pygame.K_2: self.entry_txt += "2"
                case pygame.K_3: self.entry_txt += "3"
                case pygame.K_4: self.entry_txt += "4"
                case pygame.K_5: self.entry_txt += "5"
                case pygame.K_6: self.entry_txt += "6"
                case pygame.K_7: self.entry_txt += "7"
                case pygame.K_8: self.entry_txt += "8"
                case pygame.K_9: self.entry_txt += "9"
                case pygame.K_SPACE: self.entry_txt += " "
                case pygame.K_COMMA: self.entry_txt += ","
                case pygame.K_PERIOD: self.entry_txt += "."
                case pygame.K_COLON: self.entry_txt += ":"
                case pygame.K_QUOTE: self.entry_txt += '"'
                case pygame.K_BACKSPACE:
                    tmp: list[str] = list(self.entry_txt)
                    if tmp: tmp.pop()
                    self.entry_txt = ''.join(tmp)
                case pygame.K_TAB: self.clear_input()
                case _: print("Key not recognized!")

        self.set_text(self.entry_txt, self.txt_manager.get_txtcolor())
        print("TIP: You can press TAB to clear the input.")

    def clear_input(self) -> None: 
        '''Clears the input text.'''
        self.entry_txt = ""
    
    def reset_input(self) -> None:
        '''Resets the input and writes the placeholder if there's not text and the input is not focused.
        Goes on "update" method.'''
        if len(self.text) == 0 and not self.focused:
            self.set_text(self.placeholder, self.txt_manager.get_txtcolor())

    def update(self) -> None:
        pass