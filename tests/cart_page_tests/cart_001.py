import allure
import pytest
from tests.base_test import BaseTest

@allure.epic("Cart page")
@pytest.mark.usefixtures("function_setup")
class TestCart(BaseTest):

    def choose_items(self, index):
        with allure.step(f"Choose product at index {index} and add it to cart"):
            self.catalog_page_obj.choose_product(index)
            self.product_page_obj.press_add_cart()
            self.header_area_obj.press_catalog_button()

    @allure.title("Validate empty cart message")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_cart(self):
        with allure.step("Open the cart"):
            self.header_area_obj.press_cart_button()

        with allure.step("Validate empty cart message"):
            assert self.cart_page_obj.get_empty_cart_title() == "Your cart is currently empty."

    @allure.title("Validate continue shopping button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_continue_shopping(self):
        with allure.step("Open the cart and press continue shopping"):
            self.header_area_obj.press_cart_button()
            self.cart_page_obj.press_continue_button()

        with allure.step("Validate redirect to home page"):
            assert self.home_page_obj.wait_for_url("https://madison-island.com/")

    @allure.title("Validate cart preserves selected products")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_preserves_selected_product(self):
        with allure.step("Open catalog and save first three product titles"):
            self.header_area_obj.press_catalog_button()
            first_item = self.catalog_page_obj.get_product_title(0)
            second_item = self.catalog_page_obj.get_product_title(1)
            third_item = self.catalog_page_obj.get_product_title(2)

        with allure.step("Add first three products to cart"):
            for i in range(3):
                self.choose_items(i)

        with allure.step("Open the cart"):
            self.header_area_obj.press_cart_button()

        with allure.step("Validate selected products are preserved in cart"):
            assert self.cart_page_obj.get_cart_item_title(2) == first_item
            assert self.cart_page_obj.get_cart_item_title(1) == second_item
            assert self.cart_page_obj.get_cart_item_title(0) == third_item