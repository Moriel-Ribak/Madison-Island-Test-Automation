from playwright.sync_api import Page

from components.header_area import HeaderArea
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.__header_area=HeaderArea(page)

    __PAGE_TITLE="#create_customer>h1"
    __FIRST_NAME="#FirstName"
    __LAST_NAME="#LastName"
    __EMAIL="#Email"
    __PASSWORD="#CreatePassword"
    __ERROR_MSG=".errors>ul>li"
    __CREATE_BUTTON="[value='Create']"

    def get_page_title(self):
        return self.get_text(self.__PAGE_TITLE)

    def fill_first_name(self,first_name):
        self.fill(self.__FIRST_NAME,first_name)

    def fill_last_name(self,last_name):
        self.fill(self.__LAST_NAME,last_name)

    def fill_email(self,email):
        self.fill(self.__EMAIL,email)

    def fill_password(self,password):
        self.fill(self.__PASSWORD,password)

    def press_create(self):
        self.click(self.__CREATE_BUTTON)

    def get_error_msg(self,index):
        return self.list_get_text(self.__ERROR_MSG,index)
