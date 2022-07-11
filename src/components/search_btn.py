
from util.button import Button

class SearchButton(Button):
    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        super().__init__(x, y, w, h, groups)
        self.color: str = "#65c27e"
        self.color_copy = self.color
        self.set_text("Search Wiki", "#1c1c1c")
    
    def update(self):
        self.action()
        self.scale_on_hover(1.1)
        self.change_color_on_hover("#4fab67")
        self.draw_bordered(radius=10)