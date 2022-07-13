# search page will show the result of the search on the screen

import pygame
import wikipedia
from util.text import TextEngine

class SearchPage:
    def __init__(self) -> None:
        self.txt_manager = TextEngine()

        self.search_text: str = ""
        self.txt_surf: pygame.Surface((600, 400))