# search page will show the result of the search on the screen

import pygame
import wikipedia

from util.text import TextEngine
from components.back_btn import BackButton

class SearchPage:
    def __init__(self, *groups) -> None:

        self.back_btn = BackButton(25, 25, 50, 50, groups)

        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_bg("#fdfdfd")

        self.color: str = "#fdfdfd"

        self.search_page = None
        self.search_text: str = ""
        self.txt_surf: pygame.Surface = pygame.Surface((800, 600))
        self.txt_surf.fill(self.color)

        self.search_done: bool = False
    
    def __check_search(self, txt: str) -> bool:
        try:
            self.search_page = wikipedia.page(txt)
            self.search_text = wikipedia.summary(txt)
            self.search_done = True
            return True
        except:
            # right now the error message is not displayed because it only displays when self.search_done is true
            self.txt_manager.set_txt("Couldn't make the search!")
            print("The search was not successfull.")
            self.search_done = False
            return False
    
    def __show_search(self, status: bool) -> None:
        if status:
            # TODO: make it possible to scroll if the text is to big
            # sets the title
            self.txt_manager.set_txt(self.search_page.title)
            self.txt_manager.set_font(fsize=24)
            title = self.txt_manager.render()
            self.txt_surf.blit(title, (self.txt_surf.get_width() / 2 - title.get_width() / 2, 15))

            # sets the link
            self.txt_manager.set_txt(self.search_page.url)
            self.txt_manager.set_font(fsize=10)
            url = self.txt_manager.render()
            self.txt_surf.blit(url, (self.txt_surf.get_width() / 2 - url.get_width() / 2, 50))

            # sets the content
            self.txt_manager.set_txt(self.search_text)
            self.txt_manager.set_font(fsize=16)
            search_surf = self.txt_manager.render_wrap(self.txt_surf, 25)
            self.txt_surf.blit(search_surf, (0, 50))
        else:
            # in case the search is not successful
            error_surf = self.txt_manager.render()
            self.txt_surf.blit(error_surf, (self.txt_surf.get_width() / 2 - error_surf.get_width() / 2, 
            self.txt_surf.get_height() / 2 - error_surf.get_height() / 2))

    def search(self, txt: str) -> None:
        search_status = self.__check_search(txt)
        self.__show_search(search_status)

        print("Search done.")
    
    def close_search(self) -> None:
        self.search_done = False

    def reset_search(self) -> None:
        '''Resets the search parameters.'''
        self.txt_manager.set_txt("")
        self.search_text = ""
        self.close_search()
        self.txt_surf.fill(self.color)

    def get_status(self) -> bool:
        return self.search_done        

    def get_result(self) -> pygame.Surface:
        return self.txt_surf

    def go_back(self) -> bool:
        return self.back_btn.action()