from playwright.sync_api import Page
from pages.base_page import BasePage


class HeaderArea(BasePage):

    def __init__(self,page:Page):
        super().__init__(page)

    __NAVIGATIONHEADERAREA = ".site-nav >li>a"
    __ICONSAREA = ".site-header__icons-wrapper>a"
    __SEARCHBUTTON = ".site-header__icons-wrapper>[aria-controls='SearchDrawer']"
    __SEARCH_AREA = ".search-bar__table-cell>form>input"




    def press_home_button(self):
        self.list_click(self.__NAVIGATIONHEADERAREA,0)

    def press_catalog_button(self):
        self.list_click(self.__NAVIGATIONHEADERAREA,1)

    def press_get_5_button(self):
        self.list_click(self.__NAVIGATIONHEADERAREA,2)

    def press_login_button(self):
        self.list_click(self.__ICONSAREA,0)

    def press_cart_button(self):
        self.list_click(self.__ICONSAREA,1)

    def press_search_button(self,text):
        self.click(self.__SEARCHBUTTON)
        self.fill(self.__SEARCH_AREA,text)
        self.page.press(self.__SEARCH_AREA,"Enter")



