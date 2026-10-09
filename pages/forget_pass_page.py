from playwright.sync_api import Page

from components.header_area import HeaderArea
from pages.base_page import BasePage


class ForgetPass(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.__header_area= HeaderArea(page)

    __FORGET_PASS_TITLE ="#RecoverPasswordForm>div>h2"
    __CANCEL_BUTTON = "#HideRecoverPasswordLink"

    def get_forget_pass_title(self):
        return self.get_text(self.__FORGET_PASS_TITLE)

    def press_cancel(self):
        self.click(self.__CANCEL_BUTTON)

