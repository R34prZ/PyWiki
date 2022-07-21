""" Bookmakrs screen. Displays the bookmarked search terms. """

from dis import dis
import pygame

from components.bookmark_btn import Bookmarks
from components.back_btn import BackButton
from util.text import TextEngine

class BookmarkPage:
    def __init__(self, *groups) -> None:
        self.back_btn = BackButton(25, 25, 50, 50, groups)

        self.bookmarks = Bookmarks.BOOKMARKS
        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_font(fsize=24)
        self.txt_manager.set_txt("Bookmarks")

    def display_title(self, display) -> None:
        title_surf = self.txt_manager.render()
        display.blit(title_surf, (display.get_width() / 2 - title_surf.get_width() / 2, 15))

    def display_bookmarks(self, display: pygame.Surface) -> None:
        for term in self.bookmarks:
            y = 50
            term_surf = TextEngine.render_new(term)
            display.blit(term_surf, (display.get_width() / 2 - term_surf.get_width() / 2, y))
            y += term_surf.get_height() + 10

    def go_back(self) -> bool:
        return self.back_btn.action()