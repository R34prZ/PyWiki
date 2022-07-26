import pygame

from util.text import TextEngine

class TextButton(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], txt: str = "Button", *groups) -> None:
        super().__init__(groups)

        self.pos = pygame.Vector2(*pos)

        self.txt_manager = TextEngine()
        self.txt_manager.set_txt(txt)
        self.txt_manager.set_font(fsize=18)
        self.txt_manager.set_color("#1c1c1c")
        self.txt_manager.set_bg("#fdfdfd")

        self.image = self.txt_manager.render()
        self._img_copy = self.image.copy()
        self.rect = self.image.get_rect(center=self.pos)

        self.hover: bool = False
    
    def get_size(self) -> None:
        return self.rect.size

    def check_hover(self) -> None:
        '''Checks if the button is being hovered by the cursor. Goes on "update" method.'''
        mpos = pygame.mouse.get_pos()
        
        self.hover = self.rect.collidepoint(*mpos)
    
    def check_click(self, button) -> bool:
        '''Checks if the button is being clicked by the cursor. Goes on the event loop under
        MOUSEBUTTONUP event and gets "event.button". It's necessary to reset "self.click" to false
        somewhere after the action, you can do it on on the "update" method or in the "action" method.
        Mouse buttons: 1 - left click; 2 - right click; 3 - middle click'''

        self.click = button == 1 and self.hover
        
        return self.click

    def highlight(self) -> None:
        # TODO make this work
        pass

    def update(self) -> None:
        self.check_hover()
        self.highlight()