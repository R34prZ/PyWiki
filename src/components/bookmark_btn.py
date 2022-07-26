""" Bookmarks component will handle bookmarking topics. """


from util.button import Button
from util.find_file import find

class Bookmarks(Button):
    
    BOOKMARKS: list[str] = ["pygame"]

    ICONS = {
        "empty": find("images/bookmark-empty.png"),
        "checked": find("images/bookmark-checked.png")
    }

    def __init__(self, x: int, y: int, w: float, h: float, *groups) -> None:
        super().__init__(x, y, w, h, groups)

        self.set_image(self.ICONS["empty"])

        self.checked: bool = False
        self.search_term: str = None

    def set_search_term(self, term: str) -> None:
        """ Use this to set the instace search term. The search term will be used in the
        BOOKMARKS list as reference to the bookmarked search."""
        self.search_term = term

    def display_btn(self) -> None:
        self.set_image(self.ICONS["checked"] if self.checked else self.ICONS["empty"])

    def update_status(self) -> None:
        """ Checks if the actual search term is in the bookmarks. 
            This is usefull to update the button image when searching new terms. """
        if self.search_term in Bookmarks.BOOKMARKS: self.checked = True
        else: self.checked = False
    
    def action(self) -> None:
        """ Bookmarks a search term, so it's possible to check on it later. """
        if self.hover and self.click:
            if not self.search_term in Bookmarks.BOOKMARKS:
                Bookmarks.BOOKMARKS.append(self.search_term)
                self.checked = True
            else:
                Bookmarks.BOOKMARKS.remove(self.search_term)
                self.checked = False

            self.click = False

    def update(self):
        self.check_hover()
        self.action()
        self.display_btn()
        self.update_status()








# "https://icons8.com/icon/82461/bookmark" Bookmark icon by https://icons8.com" Icons8
# "https://icons8.com/icon/3dYTLx2Bvt42/bookmark" Bookmark icon by "https://icons8.com" Icons8

