# back button

# back button image (https://icons8.com/icon/84842/back) by icons8 (https://icons8.com)

from util.find_file import find
from util.button import Button

class BackButton(Button):
    def __init__(self, x: int, y: int, w: int, h: int, *groups) -> None:
        super().__init__(x, y, w, h, groups)
        
        self.set_image(find("images/back.png"))
        
    
    def action(self) -> bool:
        if self.click:
            print("Going back...")
            return "True"

        return False

    def update(self):
        self.check_hover()
        self.scale_on_hover()
        # self.click = False