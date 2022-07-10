
import pygame

class Button(pygame.sprite.Sprite):
    ''' Base class containing the basics to make a button.'''
    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        '''It is possible to pass a "groups" parameter to put the button on a pygame group.'''
        super().__init__(*groups)
        self.pos = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.color: str = "#6448b5"

        self.image = pygame.Surface(self.size)
        self.img_copy: pygame.Surface = self.image.copy()
        self.rect = self.image.get_rect(center=self.pos)

        self.hover: bool = False
        self.click: bool = False

    def set_image(self, img: str) -> None:
        ''' Sets the image of the button. The "img" parameter needs to be a valid path to the image file.'''
        try:
            self.image = pygame.image.load(img).convert()
        except:
            raise Exception("It was not possible to change the button image. Check the path or the file extension.")
    
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
            self.image.fill(color)
        else:
            self.image.fill(self.color)

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

