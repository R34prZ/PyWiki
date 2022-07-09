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
    ''''''
    def __init__(self) -> None:
        self.txt: str = "Lorem Ipsum"

        self.fsize: int = 14
        self.font = pygame.font.SysFont("Arial", self.fsize)

        self.color: str = "#000000"
        self.AA: bool = 1
        self.txt_surf: pygame.Surface = self.font.render(self.txt, self.AA, self.color)

    def set_txt(self, txt: str) -> None:
        self.txt = txt
        self.update_surf()
    
    def set_color(self, color: str) -> None:
        self.color = color
        self.update_surf()
    
    def set_anti_aliasing(self, AA: bool) -> None:
        self.AA = AA
        self.update_surf()
    
    def set_fsize(self, fsize: int) -> None:
        self.fsize = fsize
        self.update_surf()
    
    def set_font(self, font: str) -> None:
        try:
            self.font = pygame.font.Font(font, self.fsize)
        except:
            self.font = pygame.font.SysFont(font, self.fsize)
        
        self.update_surf()
    
    def set_all(self, txt: str, color: str, font: str, fsize: int, AA: bool) -> None:
        '''Shorhand to set all the atributes in one method.'''
        self.set_txt(txt)
        self.set_color(color)
        self.set_font(font)
        self.set_fsize(fsize)
        self.set_anti_aliasing(AA)
        self.update_surf()

    def load_from_file(self, file) -> list[str]:
        '''Load text from a ".txt" file and store each line in a list entry in a variable. The "file" argument must be a valid path to a file.'''
        with open(file, "r") as f:
            self.txt = f.readlines()
        
        return self.txt

    def update_surf(self) -> None:
        '''Updates the text surface after changing any value of the atributes.'''
        self.txt_surf = self.font.render(self.txt, self.AA, self.color)

    def render(self) -> pygame.Surface:
        self.update_surf()
        return self.txt_surf

    @staticmethod
    def render_new(txt: str, font:str, fsize: int, color: str, AA: bool) -> pygame.Surface:
        '''Does the same as render_text, but it's a static method of TextEngine, meaning it can be
        used anywhere without initializing an object.'''
        try:
            font = pygame.font.Font(font, fsize)
        except:
            font = pygame.font.SysFont(font, fsize)
        
        fsurf = font.render(txt, AA, color)

        return fsurf

    

