'''Functions and classes to render and format text with pygame'''

import pygame

# pygame.font.init()


def render_text(txt: str, color: str = "#000000", font: str = "Arial", fsize: int = 14, AA: bool = False) -> pygame.Surface:
    '''Returns a pygame.Surface with text rendered to it with the specified color, font, font size. Can decide wether to
    use anti aliasing (AA) or not. Usefull for simple text rendering.'''
    try:
        font = pygame.font.Font(font, fsize)
    except:
        font = pygame.font.SysFont(font, fsize)
    
    fsurf = font.render(txt, AA, color)

    return fsurf



class TextEngine:
    ''' Powerful various functionalities to render and format text with pygame.'''
    def __init__(self) -> None:
        self.txt: str = "Lorem Ipsum"

        self.fsize: int = 14
        self.font = pygame.font.SysFont("Arial", self.fsize)

        self.color: str = "#c1c1c1"
        self.bg: str = None
        self.AA: bool = 1
        self.txt_surf: pygame.Surface = self.font.render(self.txt, self.AA, self.color, self.bg)

    def set_txt(self, txt: str) -> str:
        self.txt = txt
        self.update_surf()
        return self.txt
    
    def set_color(self, color: str) -> None:
        self.color = color
        self.update_surf()
    
    def set_anti_aliasing(self, AA: bool) -> None:
        '''Set wether to use anti aliasing to render the text or not.'''
        self.AA = AA
        self.update_surf()
    
    def set_font(self, font: str = "Arial", fsize: int = 14) -> None:
        '''Set the font and font size to use to render text.'''
        self.fsize = fsize

        try:
            self.font = pygame.font.Font(font, fsize)
        except:
            self.font = pygame.font.SysFont(font, fsize)
        
        self.update_surf()
    
    def set_bg(self, color: str | tuple) -> None:
        self.bg = color
        self.update_surf()

    def set_all(self, txt: str, color: str, font: str, fsize: int, AA: bool, bg: str | tuple) -> None:
        '''Shorhand to set all the atributes in one method.'''
        self.set_txt(txt)
        self.set_color(color)
        self.set_bg(bg)
        self.set_font(font, fsize)
        self.set_anti_aliasing(AA)
        self.update_surf()

    def get_txtcolor(self) -> str | tuple:
        return self.color

    def update_surf(self) -> None:
        '''Updates the text surface after changing any value of the atributes.'''
        self.txt_surf = self.font.render(self.txt, self.AA, self.color, self.bg)

    def load_from_file(self, file) -> list[str]:
        '''Load text from a ".txt" file and store it in a variable. The "file" argument must be a valid path to a file.'''
        with open(file, "r") as f:
            self.txt = f.read()
        
        return self.txt

    def render(self) -> pygame.Surface:
        '''Returns a pygame Surface with text rendered to it.'''
        self.update_surf()
        return self.txt_surf

    @staticmethod
    def render_new(txt: str, font:str, fsize: int, color: str, AA: bool) -> pygame.Surface:
        '''Does the same as render_text, but it's a static method of TextEngine, meaning it can be
        used anywhere TextEngine was imported, without initializing an object.'''
        try:
            font = pygame.font.Font(font, fsize)
        except:
            font = pygame.font.SysFont(font, fsize)
        
        fsurf = font.render(txt, AA, color)

        return fsurf

    def render_wrap(self, surf: pygame.Surface, padding: int = 3, line_height: int = 3,ck: tuple | str = (0, 0, 0)) -> pygame.Surface:
        '''Renders text to a pygame Surface, but break a line if the text width is greater than 
        the surface informed width. The "ck" parameter stands for colorkey and should never be the same 
        color as the font, as this will result in the text being invisible. Padding will
        only be aplied in the sides, while the top and each line will consider the font and line height.'''

        words: list[str] = self.txt.split(' ')

        fheight = self.font.get_height()
        x, y = 0 + padding, fheight + line_height

        surface = surf.copy()
        surface.fill(ck)
        surface.set_colorkey(ck)

        for word in words:
            if word == " ":
                continue
            elif word == "\n":
                x = 0 + padding
                y += (fheight + line_height)
                
            fsurf = self.font.render(word, self.AA, self.color, self.bg)

            # checks if x is greater than the surface width subtracted from the padding and break a line
            if x >= (surface.get_width() - padding) or (x + fsurf.get_width()) > surface.get_width() - padding:
                x = 0 + padding
                y += (fheight + line_height)

            surface.blit(fsurf, (x, y))
            x += fsurf.get_width()
        

        return surface