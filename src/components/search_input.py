import pygame
from util.input import Input

class SearchInput(Input):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(x, y, w, h, *groups)
        self.set_alpha(200)
    
    def update(self) -> None:
        self.draw_bordered()
        self.focus()