import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.epic("E2E")
@allure.severity(Severity.BLOCKER)
class TestE2EMan(BaseTest):

    @allure.title("E2E man product")
    @allure.description("test that check E2E man section - press the man section from home page"
                        "add item to cart and see that its shown there")
    @allure.story("The selected man product is displayed in the cart with the correct title")
    def test_add_man_product_to_cart(self):

        with allure.step("press the second don't and then shop man button"):
            self.home_page_obj.press_shop_man_button()

        with allure.step("enter the 4th product and save his name"):
            product_title = self.catalog_page_obj.get_product_title(3)
            self.catalog_page_obj.choose_product(3)

        with allure.step("add to cart"):
            self.product_page_obj.press_add_cart()

        with allure.step("go to cart"):
            self.header_area_obj.press_cart_button()

        with allure.step("check if item in cart and check if true"):
            assert self.cart_page_obj.validate_item_in_cart(product_title)

