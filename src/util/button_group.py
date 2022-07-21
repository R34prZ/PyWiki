import pygame

class BtnGroup(pygame.sprite.Group):
    """ Creates a pygame group with special methods for buttons. """

    def get_click(self, button) -> None:
        for sprite in self:
            sprite.check_click(button)

class BtnGroupSingle(pygame.sprite.GroupSingle):
    def get_click(self, button) -> None:
        for sprite in self.sprites():
            sprite.check_click(button)
