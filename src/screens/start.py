# start page (the first seen when loading PyWiki)

import pygame
from components.search_btn import SearchButton
from components.search_input import SearchInput


class Start:
    def __init__(self, *groups) -> None:
        self.search_inp = SearchInput(400, 150, 550, 50, groups)
        self.search_btn = SearchButton(400, 300, 150, 50, groups)