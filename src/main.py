
import wikipedia
import pygame
from pygame.locals import *

from screens.start import Start
from util.text import TextEngine

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

        self.btn_group = pygame.sprite.Group()
        self.start_scrn = Start(self.btn_group)
        self.txt = TextEngine()
        print(self.txt.load_from_file("./test.txt"))


    def run(self) -> None:
        while self.running:

            self.display.fill(self.bg_color)

            # events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
            # draw
            self.btn_group.draw(self.display)
            self.btn_group.update()
    
            # update
            pygame.display.flip()
            self._clock.tick(self._FPS)

if __name__ == "__main__":
    main = Main()
    main.run()



        
