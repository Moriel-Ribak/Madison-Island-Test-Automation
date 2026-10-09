import allure
import pytest
import re
from tests.base_test import BaseTest

@allure.epic("Catalog")
@pytest.mark.usefixtures("function_setup")
class TestCatalogPage(BaseTest):

    @allure.title("Validate navigation to next catalog page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_next_collection_page(self):
        with allure.step("Open catalog and navigate to the next page"):
            self.header_area_obj.press_catalog_button()
            self.catalog_page_obj.press_next_page()
        with allure.step("Validate catalog page number changed to page 2"):
            assert "2" in self.catalog_page_obj.get_page_numbers_text()

    @allure.title("Validate catalog displays correct total product count")
    @allure.severity(allure.severity_level.NORMAL)
    def test_collection_displays_product_count(self):
        with allure.step("Open catalog page"):
            self.header_area_obj.press_catalog_button()

        with allure.step("Count products across all catalog pages"):
            all_products = int(self.catalog_page_obj.count_page_products())
            self.catalog_page_obj.press_next_page()

            while True:
                all_products = all_products + int(self.catalog_page_obj.count_page_products())
                if self.catalog_page_obj.check_if_last_page():
                    break

                self.catalog_page_obj.press_next_page()

        with allure.step("Validate counted products match displayed product count"):
            assert str(all_products) in self.catalog_page_obj.get_product_count_text()

    @allure.title("Validate product cards display required details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_are_product_details_visible(self):
        with allure.step("Open catalog page"):
            self.header_area_obj.press_catalog_button()

        with allure.step("Validate product details are visible on all catalog pages"):
            list_count=self.catalog_page_obj.count_page_products()
            for i in range(list_count):
                assert self.catalog_page_obj.is_details_visible(i)

            self.catalog_page_obj.press_next_page()

            while True:
                list_count = self.catalog_page_obj.count_page_products()
                for i in range(list_count):
                    assert self.catalog_page_obj.is_details_visible(i)

                if self.catalog_page_obj.check_if_last_page():
                    break

                self.catalog_page_obj.press_next_page()

    @allure.title("Validate catalog price sorting from low to high")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sorting_control_is_available(self):
        with allure.step("Open catalog and sort products by ascending price"):
            self.header_area_obj.press_catalog_button()
            list_count=self.catalog_page_obj.count_page_products()
            self.catalog_page_obj.select_sort("price-ascending")

        with allure.step("Validate products are sorted from lowest to highest price"):
            last_product_value = 0
            for i in range(list_count):
                current_price = float(re.sub(r"[^\d.]", "",self.catalog_page_obj.get_product_price(i)))
                assert current_price >= last_product_value
                last_product_value = current_price

            self.catalog_page_obj.press_next_page()

            while True:
                list_count = self.catalog_page_obj.count_page_products()
                for i in range(list_count):
                    current_price = float(re.sub(r"[^\d.]", "", self.catalog_page_obj.get_product_price(i)))
                    assert current_price >= last_product_value
                    last_product_value = current_price

                if self.catalog_page_obj.check_if_last_page():
                    break

                self.catalog_page_obj.press_next_page()