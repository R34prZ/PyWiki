import pygame

class InpGroup(pygame.sprite.Group):
    """ Creates a pygame group with special methods for inputs. """
    def __init__(self) -> None:
        super().__init__()

    def handle_input(self, key) -> None:
        for sprite in self.sprites():
            sprite.get_input(key)