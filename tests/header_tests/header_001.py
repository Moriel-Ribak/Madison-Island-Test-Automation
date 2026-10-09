import time

import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.epic("Header")
@allure.severity(Severity.CRITICAL)
class TestHomePageNavigations(BaseTest):
        @allure.description("Press any header and validate pages")
        @allure.title("Header navigations checks")
        @allure.story("Header pages open")

        def test_navigate_cart(self):
            with allure.step("press the cart section and checks title"):
                self.header_area_obj.press_cart_button()
                with allure.step("checks if the cart product row is visible - if not"
                                 "take the empty cart title var instead"):
                    if  self.cart_page_obj.card_row_visible():
                        assert self.cart_page_obj.get_cart_title() == "Your cart"
                    else:
                        assert self.cart_page_obj.get_empty_cart_title() == "Your cart is currently empty."

        def test_navigate_login(self):
            with allure.step("press the login section and checks title"):
                self.header_area_obj.press_login_button()
                assert self.login_page_obj.get_login_title() == "Login"

        def test_navigate_search(self):
            with allure.step("press the search section type and press enter"):
                with allure.step("checks if the item list is visible when there is items to show"):
                    self.header_area_obj.press_search_button("s")
                    assert self.catalog_page_obj.search_results_visible()

                with allure.step("checks if the item list is not visible when there is no items to show"):
                    self.header_area_obj.press_search_button("shoes")
                    assert not self.catalog_page_obj.search_results_visible()

        def test_navigate_catalog(self):
            with allure.step("press the catalog section and checks title"):
                self.header_area_obj.press_catalog_button()
                assert self.catalog_page_obj.get_title() == "Products"

        def test_navigate_home(self):
            with allure.step("press the Home section and checks home page objects"):
                self.header_area_obj.press_home_button()
                assert self.home_page_obj.get_url() == "https://madison-island.com/"
                assert self.home_page_obj.collection_list_title() == "COLLECTION LIST"
                assert self.home_page_obj.collection_visible() == True
                assert self.home_page_obj.slideshow_visible() == True

        def test_navigate_get5(self):
            with allure.step("press get 5$ section and checks title"):
                self.header_area_obj.press_get_5_button()
                time.sleep(5)
                assert self.get_5_page_obj.get5_title() == "GIVE\xa0$5, GET\xa0$5!"


