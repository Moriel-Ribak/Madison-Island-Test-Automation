from _testcapi import awaitType

from components.header_area import HeaderArea
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.__header_area = HeaderArea(page)


    __EMAIL = "#CustomerEmail"
    __PASSWORD = "#CustomerPassword"
    __FORGET_PASS ="[id='RecoverPassword']"
    __SIGN_IN = "[value='Sign In']"
    __CREATE_ACC = "#customer_register_link"
    __LOGIN_TITLE= "#customer_login>h1"
    __MY_ACCOUNT_TITLE=".section-header>h1"
    __ERROR_MSG= ".errors>ul>li"
    __FORGET_PASS_BUTTON = "#RecoverPassword"
    __REGISTER_BUTTON = "#customer_register_link"



    def login(self,email,password):
        self.fill(self.__EMAIL,email)
        self.fill(self.__PASSWORD, password)
        self.click(self.__SIGN_IN)

    def get_login_title(self):
        return self.get_text(self.__LOGIN_TITLE)

    def get_error_msg(self):
        return self.get_text(self.__ERROR_MSG)


    def get_my_account_title(self):
        return self.get_text(self.__MY_ACCOUNT_TITLE)

    def click_forget_password(self):
        self.click(self.__FORGET_PASS_BUTTON)

    def click_register(self):
        self.click(self.__REGISTER_BUTTON)
