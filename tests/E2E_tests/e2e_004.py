import time
import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.severity(Severity.BLOCKER)
@allure.epic("E2E")
class TestE2EQuantity(BaseTest):

    @allure.title("E2E Quantity")
    @allure.description("Adding item to cart changing the quantity and validating it changed")
    @allure.story("Cart quantity is updated and the total reflects the new quantity")
    def test_e2e_Quantity(self):
        with allure.step("Navigate to all products and enter the fourth item"):
            self.header_area_obj.press_catalog_button()
            self.catalog_page_obj.choose_product(5)

        with allure.step("Add item to cart"):
            self.product_page_obj.press_add_cart()

        with allure.step("change quantity in item to cart"):
            quantity = "4"
            self.cart_page_obj.change_quantity(quantity)
            time.sleep(4)


        with allure.step("Validate quantity changed"):
            assert self.cart_page_obj.get_quantity_value() == quantity






