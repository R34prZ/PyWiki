
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
        self.txt_manager.set_color("#c1c1c1")
        self.text: str = "Input"

        self.focused: bool = True

        self.set_text()
    
    def set_image(self, img: str) -> None:
        try:
            self.image = pygame.image.load(img).convert()
        except:
            raise Exception("It was not possible to change the input image. Check the path or the file extension.")
    
    def draw_bordered(self, radius: int = 50) -> None:
        '''Draws the input with rounded borders.'''
        img_copy = self.image.copy()
        img_copy.fill("#000000")
        img_copy.set_colorkey("#000000")

        self.border_radius = radius
        pygame.draw.rect(img_copy, self.color, (0, 0, *self.rect.size), border_radius = self.border_radius)

        self.image = img_copy
        self.update_surf()
    
    def focus(self, bcolor: str = "#8f3af0", width: int = 3) -> None:
        '''Draws a border into the input if it got focus (got clicked or hovered).'''
        mpos = pygame.mouse.get_pos()
        img_copy = self.image.copy()

        if self.rect.collidepoint(*mpos):
            # can use if pygame.mouse.get_pressed()[0] to focus only on press
            pygame.draw.rect(img_copy, bcolor, (0, 0, *self.rect.size), width, self.border_radius)
            self.image = img_copy
            self.focused = True
        
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

    def update(self) -> None:
        pass