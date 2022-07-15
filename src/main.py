#!/usr/bin/env python3

"""main.py: the main function, run this to launch the program."""

__author__ = "R34prZ"


import threading

import pygame
from pygame.locals import *

from screens.start import StartPage
from screens.search import SearchPage

from util.input_group import InpGroup
from util.button_group import BtnGroup

pygame.init()

class Main:
    NAME: str = "PyWiki"
    WIDTH: int = 800
    HEIGHT: int = 600

    def __init__(self) -> None:
        self.size: int = (self.WIDTH, self.HEIGHT)

        self.display: pygame.Surface = pygame.display.set_mode(self.size, 0, 32)
        pygame.display.set_caption(self.NAME)

        self._clock = pygame.time.Clock()
        self._FPS: float = 60

        self.running: bool = True

        self.bg_color: str = "#fdfdfd"  

        self.btn_group = BtnGroup()
        self.inp_group = InpGroup()
        self.back_btn_group = BtnGroup()

        self.start_scrn = StartPage(self.inp_group, self.btn_group)
        self.search_scrn = SearchPage(self.back_btn_group)

        self.actual_screen: str = "start"

    def run(self) -> None:
        while self.running:

            self.display.fill(self.bg_color)

            # events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()

                    self.inp_group.handle_input(event.key)

                elif event.type == MOUSEBUTTONUP:
                    self.btn_group.get_click(event.button)
                    self.back_btn_group.get_click(event.button)
                
                elif event.type == pygame.USEREVENT + 1:
                    print("searching...")
                    self.actual_screen = "search"
                    # starts another thread, so the program wont entirely stop while searching
                    threading.Thread(target=self.search_scrn.search, args=(self.start_scrn.get_search_value(),)).start()
                   
            # draw
            if self.actual_screen == "start":
                self.btn_group.draw(self.display)
                self.inp_group.draw(self.display)

            elif self.actual_screen == "search":
                if self.search_scrn.get_status():
                    self.display.blit(self.search_scrn.get_result(), (0, 0))
                if self.search_scrn.go_back():
                    self.search_scrn.reset_search()
                    self.actual_screen = "start"

                self.back_btn_group.draw(self.display)

            
            # update
            # TODO fix the buttons being clickable on other screens
            self.btn_group.update()
            self.back_btn_group.update()
            self.inp_group.update()

            pygame.display.flip()
            self._clock.tick() # won't cap FPS for now

if __name__ == "__main__":
    main = Main()
    main.run()
