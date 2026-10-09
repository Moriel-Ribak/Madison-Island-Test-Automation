from pages.base_page import BasePage


class Get5Page(BasePage):

    def __init__(self,page):
        super().__init__(page)

    __GET5_TITLE = ".header>h1"


    def get5_title(self):
        frame = self.page.frame_locator("[name='talkable-offer-iframe']")
        title = frame.locator(".header > h1").inner_text()

        return title