""" The first screen seen in PyWiki, and the one from where the user makes their search."""

from components.search_btn import SearchButton
from components.search_input import SearchInput
from components.go_to_bookmarks import GoBookmarking
from util.text import render_text

class StartPage:
    def __init__(self, *groups) -> None:
        self.search_inp = SearchInput(400, 150, 550, 50, groups[0])
        self.search_btn = SearchButton(400, 300, 150, 50, groups[1])
        self.bookmarking_btn = GoBookmarking(400, 550, 100, 30, groups[1])
    
    def display_tip(self, display) -> None:
        suggestion = render_text("TIP: You can clear the input text with TAB.", "#1c1c1c", fsize=12, AA=1)
        display.blit(suggestion, (display.get_width() / 2 - suggestion.get_width() / 2, 180))

    def get_search_value(self) -> str:
        return self.search_inp.get_value()