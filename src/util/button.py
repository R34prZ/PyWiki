
import pygame
from util.text import TextEngine

class Button(pygame.sprite.Sprite):
    ''' Base class containing the basics to make a button.'''
    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        '''It is possible to pass a "groups" parameter to put the button on a pygame group.'''
        super().__init__(*groups)
        self.pos = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.color: str = "#6448b5"
        self.color_copy: str = self.color
        self.border_radius: int = 0

        self.image = pygame.Surface(self.size)
        self.img_copy: pygame.Surface = self.image.copy()
        self.rect = self.image.get_rect(center=self.pos)

        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#c1c1c1")
        self.text: str = "Button"

        self.hover: bool = False
        self.click: bool = False

    def set_image(self, img: str) -> None:
        ''' Sets the image of the button. The "img" parameter needs to be a valid path to the image file.'''
        try:
            self.image = pygame.image.load(img).convert()
        except:
            raise Exception("It was not possible to change the button image. Check the path or the file extension.")
    
    def set_text(self, txt: str = "Button", color: str | tuple = "#c1c1c1") -> None:
        self.text = txt
        self.txt_manager.set_txt(self.text)
        self.txt_manager.set_color(color)
        
        img_copy = self.image.copy()
        txt_surf = self.txt_manager.render()
        img_copy.blit(txt_surf, (self.rect.width / 2 - txt_surf.get_width() / 2, self.rect.height / 2 - txt_surf.get_height() / 2))
        self.image = img_copy

    def scale_on_hover(self, scale_factor: float = 1.2) -> None:
        mpos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(*mpos):
            self.image = pygame.transform.smoothscale(self.img_copy, self.size * scale_factor)
            self.rect = self.image.get_rect(center=self.pos)
            self.hover = True
        else: 
            self.image = pygame.transform.smoothscale(self.img_copy, self.size)
            self.rect = self.image.get_rect(center=self.pos)
            self.hover = False

    def change_color_on_hover(self, color: str) -> None:
        if self.hover:
            self.color = color
            self.image.fill(self.color)
        else:
            self.color = self.color_copy
            self.image.fill(self.color)

    def draw_bordered(self, radius: int = 50) -> None:
            '''Draws the button with rounded borders.'''
            img_copy = self.image.copy()
            img_copy.fill("#000000")
            img_copy.set_colorkey("#000000")

            self.border_radius = radius
            pygame.draw.rect(img_copy, self.color, (0, 0, *self.rect.size), border_radius = self.border_radius)

            self.image = img_copy
            self.update_surf()

    def update_surf(self) -> None:
        '''Updates the input surface (self.image).'''
        # self.set_alpha(self.alpha)
        self.set_text(self.text, self.txt_manager.color)

    def action(self) -> None:
        '''Method to be overloaded with the action the button will perform.'''
        mpos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(*mpos):
            self.click = True
        elif self.click:
            self.click = False
            print("Click click you pressed a button!")

    def update(self):
        pass

