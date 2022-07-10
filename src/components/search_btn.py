
from util.button import Button

class SearchButton(Button):
    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        super().__init__(x, y, w, h, groups)
        self.color: str = "#65c27e"
    
    def update(self):
        self.action()
        self.scale_on_hover()
        self.change_color_on_hover("#4fab67")