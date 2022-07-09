import pygame

class Input(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(x, y)
        self.size = pygame.Vector2(w, h)

        self.image: pygame.Surface = pygame.Surface(self.size)
        self.rect: pygame.Rect = self.image.get_rect(center=self.pos)

        self.color: str = "#6448b5"

        self.placeholder: str = "Placeholder"

    def change_color(self, color: str) -> None:
        self.image.fill(color)

    def focus(self) -> None:
        '''Implement borders around the image'''
        pass

    def update(self) -> None:
        pass