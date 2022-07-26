
from util.input import Input

class SearchInput(Input):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(x, y, w, h, *groups)
        self.set_alpha(200)
        self.set_text(self.placeholder, self.txt_manager.get_txtcolor())

    def get_value(self) -> str:
        if self.text != self.placeholder:
            return self.text
        return "pygame"
    
    def update(self) -> None:
        self.draw_bordered()
        self.focus()
        self.reset_input()