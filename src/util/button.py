import pygame

class Button(pygame.sprite.Sprite):
    ''' Base class containing the basics to make a button.'''
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        '''It is possible to pass a "groups" parameter to put the button on a pygame group.'''
        super().__init__(*groups)
        self.pos = pygame.Vector2(x, y)
        self.size: list = [w, h]

        self.color: str = "#6448b5"

        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(center=self.pos)

        self.hover: bool = False

    def set_image(self, img) -> None:
        ''' Sets the image of the button. The "img" parameter needs to be a valid path to the image file.'''
        try:
            self.image = pygame.image.load(img)
        except:
            raise Exception("It was not possible to change the button image. Check the path or the file extension.")
    
    def scale_on_hover(self) -> None:
        pass
        '''if hovering -> scale logic and self.hover = true; else -> self.hove = false'''

    def change_color_on_hover(self, color: str) -> None:
        if self.hover:
            self.image.fill(color)
        else:
            self.image.fill(self.color)

    def update(self):
        pass

