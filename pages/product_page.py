from playwright.sync_api import Page
from components.header_area import HeaderArea
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.__header_area = HeaderArea(page)

    __ADD_CART_BUTTON="[name='add']"
    __PRODUCT_TITLE = ".product-single__title"
    __PRODUCT_PRICE = ".price-item.price-item--regular"
    __SIZE_LIST="#SingleOptionSelector-0"
    __SIZE_LIST_OPTION="#SingleOptionSelector-0>option"
    __SIZE_LIST_SELECTED="#SingleOptionSelector-0>[selected='selected']"
    __COLOR_LIST="#SingleOptionSelector-1"
    __COLOR_LIST_OPTION="#SingleOptionSelector-1>option"
    __COLOR_LIST_SELECTED="#SingleOptionSelector-1>[selected='selected']"


    def press_add_cart(self):
        self.click(self.__ADD_CART_BUTTON)

    def get_product_title(self):
        return self.get_text(self.__PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_text(self.__PRODUCT_PRICE)

    def choose_size(self,list_row):
        self.page.locator(self.__SIZE_LIST).select_option(index=list_row)

    def get_selected_size(self):
        return self.get_text(self.__SIZE_LIST_SELECTED)

    def get_option_size(self,list_row):
        return self.list_get_text(self.__SIZE_LIST_OPTION,list_row)

    def choose_color(self,list_row):
        self.page.locator(self.__COLOR_LIST).select_option(index=list_row)

    def get_selected_color(self):
        return self.get_text(self.__COLOR_LIST_SELECTED)

    def get_option_color(self,list_row):
        return self.list_get_text(self.__COLOR_LIST_OPTION,list_row)

