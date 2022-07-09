# start page (the first seen when loading PyWiki)

import pygame
from components.search_btn import SearchButton


class Start:
    def __init__(self, *groups) -> None:
        self.search_btn = SearchButton(400, 300, 100, 50, groups)