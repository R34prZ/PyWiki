#!/usr/bin/env python3

"""main.py: the main function, run this to launch the program."""

__author__ = "R34prZ"


import threading

import pygame
from pygame.locals import *

from screens.start import StartPage
from screens.search import SearchPage
from screens.bookmarks import BookmarkPage

from util.input_group import InpGroup
from util.button_group import BtnGroup
from util.text import TextEngine

pygame.init()

class Main:
    NAME: str = "PyWiki"
    WIDTH: int = 800
    HEIGHT: int = 600

    def __init__(self) -> None:
        self.size: int = (self.WIDTH, self.HEIGHT)

        self.display: pygame.Surface = pygame.display.set_mode(self.size, 0, 32)
        self.set_caption(self.NAME)

        self._clock = pygame.time.Clock()
        self._FPS: float = 60

        self.running: bool = True

        self.bg_color: str = "#fdfdfd"  

        self.btn_group = BtnGroup()
        self.inp_group = InpGroup()
        self.back_btn_group = BtnGroup()
        self.bookmarks_group = BtnGroup()

        self.start_scrn = StartPage(self.inp_group, self.btn_group)
        self.search_scrn = SearchPage(self.back_btn_group, self.bookmarks_group)
        self.bookmark_scrn = BookmarkPage(self.back_btn_group)

        self.actual_screen: str = "start"

    def set_caption(self, caption: str) -> None:
        pygame.display.set_caption(caption)

    def handle_events(self) -> None:
        """ Handle all the events. """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            
                # handle typing on input
                self.inp_group.handle_input(event.key)
            
            # handle scroll event
            elif event.type == MOUSEBUTTONDOWN:
                # page scroll with mouse events
                if event.button == 4: TextEngine.SCROLL_Y += 50
                elif event.button == 5: TextEngine.SCROLL_Y -= 50

            # handle click event
            elif event.type == MOUSEBUTTONUP:
                self.btn_group.get_click(event.button)
                self.back_btn_group.get_click(event.button)
                self.bookmarks_group.get_click(event.button)
            
            # handles the SEARCH_WIKIPEDIA event
            elif event.type == USEREVENT + 1:
                print("searching...")
                self.actual_screen = "search"
                print("Starting thread to search...")
                # starts another thread, so the program wont entirely stop while searching
                self.search_scrn.start_loading()
                if threading.active_count() == 1:
                    threading.Thread(target=self.search_scrn.search, args=(
                        self.start_scrn.get_search_value(),)).start()

                    print(f"Active threads: {threading.active_count()}")
            
            # handles the GO_TO_BOOKMARKS event
            elif event.type == USEREVENT + 2:
                self.actual_screen = "bookmarks"
                print("Going to bookmarks...")

    def draw(self) -> None:
        """ Draws everything to the screen."""
        if self.actual_screen == "start":
            self.btn_group.draw(self.display)
            self.inp_group.draw(self.display)
            self.start_scrn.display_tip(self.display)
            self.set_caption(self.NAME)

        elif self.actual_screen == "search":
            # display "searching" message before getting the result
            if self.search_scrn.get_loading():
                self.search_scrn.display_loading(self.display)
                self.set_caption(f"{self.NAME} | searching...")
            
            # if the search was successful, get the it and display it
            if self.search_scrn.get_status():
                TextEngine.scroll(self.search_scrn.get_result(), self.display, -600)
                self.set_caption(f"{self.NAME} | {self.start_scrn.get_search_value()}")
                self.bookmarks_group.draw(self.display)
                self.bookmarks_group.update()
            elif not self.search_scrn.get_status() and threading.active_count() == 1:
                self.search_scrn.update_surface()
                self.search_scrn.display_error(self.display)

            if self.search_scrn.go_back():
                self.search_scrn.reset_search()
                self.actual_screen = "start"
                
            
            self.back_btn_group.draw(self.display)

        elif self.actual_screen == "bookmarks":
            self.bookmark_scrn.display_title(self.display)
            self.bookmark_scrn.display_bookmarks(self.display)
            self.set_caption(f"{self.NAME} | Bookmarks")

            if self.bookmark_scrn.go_back():
                self.actual_screen = "start"

            self.back_btn_group.draw(self.display)
            self.bookmark_scrn.update()

    def run(self) -> None:
        while self.running:

            self.display.fill(self.bg_color)

            # events
            self.handle_events()
                   
            # draw
            self.draw()

            # update
            # TODO fix the buttons being clickable on other screens
            self.btn_group.update()
            self.inp_group.update()

            self.back_btn_group.update()
    
            pygame.display.flip()
            self._clock.tick(120)

if __name__ == "__main__":
    main = Main()
    main.run()