""" Bookmakrs screen. Displays the bookmarked search terms. """

import pygame

from components.bookmark_btn import Bookmarks
from components.back_btn import BackButton
from util.text import TextEngine
from util.text_button import TextButton
from util.button_group import BtnGroup

class BookmarkPage:
    def __init__(self, *groups) -> None:
        self.back_btn = BackButton(25, 25, 50, 50, groups)

        self.bookmarks = Bookmarks.BOOKMARKS
        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_font(fsize=24)
        self.txt_manager.set_txt("Bookmarks")

        self.terms_group = BtnGroup()

    def display_title(self, display) -> None:
        title_surf = self.txt_manager.render()
        display.blit(title_surf, (display.get_width() / 2 - title_surf.get_width() / 2, 15))

    def display_bookmarks(self, display: pygame.Surface) -> None:
        y = 80
        for term in sorted(self.bookmarks):
            favorite_term = TextButton((display.get_width() / 2, y), term, self.terms_group)

            y += favorite_term.get_size()[1] + 10

        self.terms_group.draw(display)

    def go_back(self) -> bool:
        return self.back_btn.action()

    def update(self) -> None:
        self.terms_group.update()