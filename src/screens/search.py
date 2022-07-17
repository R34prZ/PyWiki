""" The search page will show the result of the search on the screen. """

import pygame
import wikipedia

from util.text import TextEngine
from components.back_btn import BackButton

class SearchPage:
    def __init__(self, *groups) -> None:
        """ Initializes the search page. The page's screen will have 1200px height, meaning
        this is the most it can display in text."""
        self.back_btn = BackButton(25, 25, 50, 50, groups)

        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_bg("#fdfdfd")

        self.color: str = "#fdfdfd"

        self.search_page = None
        self.search_text: str = ""
        self.txt_surf: pygame.Surface = pygame.Surface((800, 1200)) # limits to 1200px height to be able to show more text
        self.txt_surf.fill(self.color)

        self.search_done: bool = False
        self.loading: bool = False
    
    def __check_search(self, txt: str) -> bool:
        try:
            self.search_page = wikipedia.page(txt)
            self.search_text = wikipedia.summary(txt)
            self.search_done = True
            return True
        except wikipedia.exceptions.DisambiguationError:
            self.txt_manager.set_txt(f'"{txt}" may refer to more than one result. Be more specific.')
        except wikipedia.exceptions.PageError:
            self.txt_manager.set_txt(f'{txt} does not match any wikipedia page.')
        except:
            self.txt_manager.set_txt("The search was not successful.")
        
        print("The search was not successfull.")
        self.search_done = False
        return False
    
    def __show_search(self, status: bool) -> None:
        self.update_surface()
        if status:
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
            search_surf = self.txt_manager.render_wrap(self.txt_surf, 30)
            self.txt_surf.blit(search_surf, (0, 50))

    def display_error(self, display: pygame.Surface) -> None:
        '''In case the search is not successful, shows a generic error message.
        The message is defined at "__check_search" method.'''
        self.txt_manager.set_font(fsize=24)
        error_surf = self.txt_manager.render()
        display.blit(error_surf, (display.get_width() / 2 - error_surf.get_width() / 2, 
        display.get_height() / 2 - error_surf.get_height() / 2))

    def display_loading(self, display: pygame.Surface) -> None:
        '''Displays a generic loading message.'''
        load_surf = self.txt_manager.render_new("searching...", fsize=24)
        display.blit(load_surf, (display.get_width() / 2 - load_surf.get_width() / 2, 
            display.get_height() / 2 - load_surf.get_height() / 2))

    def search(self, txt: str) -> None:
        search_status: bool = self.__check_search(txt)
        self.__show_search(search_status)
        self.loading = False
        print("Search done.")

    def close_search(self) -> None:
        self.search_done = False

    def update_surface(self) -> None:
        self.txt_surf.fill(self.color)

    def reset_search(self) -> None:
        '''Resets the search parameters.'''
        self.txt_manager.set_txt("")
        self.search_text = ""
        self.close_search()
        self.update_surface()

    def get_status(self) -> bool:
        return self.search_done        

    def get_result(self) -> pygame.Surface:
        return self.txt_surf

    def start_loading(self) -> None:
        self.loading = True
    
    def get_loading(self) -> bool:
        return self.loading

    def go_back(self) -> bool:
        return self.back_btn.action()