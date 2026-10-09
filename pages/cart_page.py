import allure
from playwright.sync_api import Page

from components.header_area import HeaderArea
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self,page:Page):
        super().__init__(page)
        self.__header_area=HeaderArea(page)


    __CART_PRODUCTS="tbody>.cart__row"
    __CARD_ROW = ".cart__row"
    __CART_PRODUCT_TITLE="tbody>.cart__row>td>div>a"
    __PRODUCT_QUANTITY = "[name='updates[]']"
    __CART_TITLE = ".section-header>h1"
    __EMPTY_CART_TITLE = ".empty-page-content>p"
    __PRODUCT_DETAILS = ".cart__meta-text"
    __CONTINUE_BUTTON =".empty-page-content>a"
    __CART_ITEM_TITLE =".list-view-item__title>a"

    def get_cart_product_name(self,index):
        return self.list_get_text(self.__CART_PRODUCT_TITLE,index)


    @allure.step("Check if product '{product_title}' exists in cart")
    def validate_item_in_cart(self,product_title):
        cart_range= self.count(self.__CART_PRODUCTS)

        for i in range(cart_range):
            cart_product_name=self.get_cart_product_name(i-1)
            if cart_product_name == product_title:
                return True
            break
        return False

    def change_quantity(self, number):
        quantity = self.page.locator(self.__PRODUCT_QUANTITY)
        quantity.fill(str(number))
        quantity.press("Enter")


    def get_quantity_value(self):
        return self.get_attribute(self.__PRODUCT_QUANTITY,"value")

    def get_cart_title(self):
        return self.get_text(self.__CART_TITLE)

    def get_empty_cart_title(self):
        return self.get_text(self.__EMPTY_CART_TITLE)

    def card_row_visible(self):
        return self.is_visible(self.__CARD_ROW)

    def get_product_details(self):
        return self.get_text(self.__PRODUCT_DETAILS)

    def press_continue_button(self):
        self.click(self.__CONTINUE_BUTTON)

    def get_cart_item_title(self,index):
        return self.list_get_text(self.__CART_ITEM_TITLE,index)