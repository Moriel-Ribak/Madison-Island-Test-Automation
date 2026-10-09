import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.epic("E2E")
@allure.severity(Severity.BLOCKER)
class TestE2EWomen(BaseTest):

    @allure.description("test that check E2E womans section - press the woman section from home page "
                        "add item to cart and see that its shown there")
    @allure.title("E2E woman product")
    @allure.story("The selected Women product is displayed in the cart with the correct title")
    def test_add_woman_product_to_cart(self):

        with allure.step("press the second dot and press the shop woman button"):
            self.home_page_obj.press_dots(1)
            self.home_page_obj.press_shop_woman_button()

        with allure.step("enter the fourth product and save his title"):
            product_title = self.catalog_page_obj.get_product_title(3)
            self.catalog_page_obj.choose_product(3)

        with allure.step("add to cart"):
            self.product_page_obj.press_add_cart()

        with allure.step("navigate to cart"):
            self.header_area_obj.press_cart_button()

        assert self.cart_page_obj.validate_item_in_cart(product_title)==True

