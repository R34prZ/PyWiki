
import pygame
from util.button import Button


class SearchButton(Button):
    
    __search_event = pygame.USEREVENT + 1
    SEARCH_WIKIPEDIA = pygame.event.Event(__search_event)

    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        super().__init__(x, y, w, h, groups)
        self.color: str = "#65c27e"
        self.color_copy = self.color
        self.set_text("Search Wiki", "#1c1c1c")

    def action(self) -> None:
        '''Places SEARCH_WIKIPEDIA event on the queue as "pygame.USEREVENT + 1", so it
        can be retrieved in the main loop and used to search for information.'''
        if self.click:
            pygame.event.post(self.SEARCH_WIKIPEDIA)
            self.click = False
    
    def update(self):
        self.check_hover()
        self.action()
        self.scale_on_hover(1.1)
        self.change_color_on_hover("#4fab67")
        self.draw_bordered(radius=10)