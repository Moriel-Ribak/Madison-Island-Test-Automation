import allure
import pytest
from tests.base_test import BaseTest

@allure.epic("Header")
@pytest.mark.usefixtures("function_setup")
class TestSearchTest(BaseTest):

    @allure.title("Validate search for an existing product")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_known_product(self):
        with allure.step("Search for an existing product"):
            self.header_area_obj.press_search_button("LUDLOW SHEATH DRESS")

        with allure.step("Validate the correct product is displayed in search results"):
            assert self.catalog_page_obj.get_search_list_item_title() == "LUDLOW SHEATH DRESS"

    @allure.title("Validate search for a non-existing product")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_non_existing_product(self):
        with allure.step("Search for a product that does not exist"):
            self.header_area_obj.press_search_button("ERROR")

        with allure.step("Validate no products are displayed in search results"):
            assert self.catalog_page_obj.get_search_list_count() == 0