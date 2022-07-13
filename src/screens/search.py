# search page will show the result of the search on the screen

import pygame
import wikipedia
from util.text import TextEngine

class SearchPage:
    def __init__(self) -> None:
        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_bg("#fdfdfd")

        self.search_text: str = ""
        self.txt_surf: pygame.Surface = pygame.Surface((800, 600))
        self.txt_surf.fill("#fdfdfd")

        self.search_done: bool = False
    
    def search(self, txt: str) -> str:
        search = wikipedia.page(txt)
        try:
            self.search_text = str(wikipedia.summary(txt))
            self.search_done = True
        except:
            self.txt_manager.set_txt("Couldn't make the search!")
            print("The search was not successfull.")
            self.search_done = False

        self.txt_manager.set_txt(search.title)
        self.txt_manager.set_font(fsize=24)
        title = self.txt_manager.render()
        self.txt_surf.blit(title, (self.txt_surf.get_width() / 2 - title.get_width() / 2, 15))

        self.txt_manager.set_txt(self.search_text)
        self.txt_manager.set_font(fsize=16)
        search_surf = self.txt_manager.render_wrap(self.txt_surf, 25)
        self.txt_surf.blit(search_surf, (0, 40))
        print(self.txt_manager.get_txt())

        return self.txt_manager.get_txt()
    
    def close_search(self) -> None:
        self.search_done = False

    def get_status(self) -> bool:
        return self.search_done        

    def get_result(self) -> pygame.Surface:
        return self.txt_surf
