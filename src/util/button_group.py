import pygame

class BtnGroup(pygame.sprite.Group):
    def __init__(self, *sprites) -> None:
        super().__init__(*sprites)

    def get_click(self, button) -> None:
        for sprite in self.sprites():
            sprite.check_click(button)