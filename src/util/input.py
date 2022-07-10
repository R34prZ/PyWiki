
import pygame
from util.text import TextEngine

class Input(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.image: pygame.Surface = pygame.Surface(self.size)
        self.rect: pygame.Rect = self.image.get_rect(center=self.pos)

        self.color: str = "#1c1c1c"
        self.alpha: int = 255

        self.image.fill(self.color)
        self.image.set_alpha(self.alpha)

        self.txt_manager = TextEngine()
        self.txt_manager.set_color("#c1c1c1")
        self.text: str = "Placeholder"

        self.set_text()

    def set_color(self, color: str = "#1c1c1c") -> None:
        self.image.fill(color)
    
    def set_alpha(self, alpha: int = 255) -> None:
        ''' Set the image alpha (transparency). The "alpha" parameter needs to be an integer ranging
        from 0 to 255.'''
        self.alpha = alpha
        self.image.set_alpha(self.alpha)
    
    def set_text(self, txt: str = "Placeholder", color: str | tuple = "#c1c1c1") -> None:
        self.text = txt
        self.txt_manager.set_txt(self.text)
        self.txt_manager.set_color(color)
        
        img_copy = self.image.copy()
        txt_surf = self.txt_manager.render()
        img_copy.blit(txt_surf, (self.rect.width / 2 - txt_surf.get_width() / 2, self.rect.height / 2 - txt_surf.get_height() / 2))
        self.image = img_copy

    def focus(self) -> None:
        '''Implement borders around the image'''
        pass

    def update(self) -> None:
        pass