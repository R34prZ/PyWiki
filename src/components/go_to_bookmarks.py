
import pygame
from util.button import Button

class GoBookmarking(Button):

    __bookmark_event = pygame.USEREVENT + 2 
    GO_TO_BOOKMARKS = pygame.event.Event(__bookmark_event)

    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        super().__init__(x, y, w, h, groups)
        self.color = "#20211e"
        self.color_copy = self.color
        self.set_text("Bookmarks")

    def action(self) -> None:
        if self.click:
            pygame.event.post(self.GO_TO_BOOKMARKS)
            self.click = False

    def update(self):
        self.check_hover()
        self.action()
        self.scale_on_hover(1.1)
        self.change_color_on_hover("#141413")
        self.draw_bordered(radius=5)