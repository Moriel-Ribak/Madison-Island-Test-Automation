import allure
import pytest
from allure_commons.types import Severity
from pages.base_page import BasePage
from tests.base_test import BaseTest
from util.config import ConfigReader


@pytest.mark.usefixtures("function_setup")
@allure.severity(Severity.BLOCKER)
@allure.epic("E2E")
class TestE2ELogin(BaseTest):

    valid_user = ConfigReader.read_list("users", "valid_user")

    @allure.title("E2E Login")
    @allure.description("Login, add item and validate it in cart")
    @allure.story("User logs in successfully and the selected product is shown correctly in the cart")
    @pytest.mark.parametrize("email,password",valid_user)
    def test_login_add_item(self,email,password):

        with allure.step("log in to site"):
            self.header_area_obj.press_login_button()
            self.login_page_obj.login(email,password)

        with allure.step("nevigate to all products and add the first item and save title"):
            self.header_area_obj.press_catalog_button()
            product_title = self.catalog_page_obj.get_product_title(0)
            self.catalog_page_obj.choose_product(0)


        with allure.step("add item to cart"):
            self.product_page_obj.press_add_cart()

        with allure.step("validate item in cart"):
            assert self.cart_page_obj.validate_item_in_cart(product_title)

