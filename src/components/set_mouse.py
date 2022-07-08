import pygame

class Mouse(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(0, 0)

        self.image: pygame.Surface = None
        try: self.rect = self.image.get_rect(center=self.pos)
        except: print("Custom cursor image not defined.")

    @staticmethod
    def set_visibility(visible: bool = True) -> None:
        '''If visible is True, the default OS cursor will appear. Set to False to hide it.'''
        pygame.mouse.set_visible(visible)
    
    def set_pos(self) -> None:
        '''Needs to be put on "update" method in order to update the position.'''
        self.pos = pygame.mouse.get_pos()
    
    def get_pos(self) -> pygame.Vector2:
        return self.pos
    
    def set_image(self, img: str) -> None:
        '''The "img" parameter needs to be a valid path to an image file.'''
        try:
            self.image = pygame.image.load(img)
        except:
            raise Exception("Invalid custom cursor image. Either the file format is not supported or the path is wrong.")
    
    def update(self) -> None:
        self.set_pos()