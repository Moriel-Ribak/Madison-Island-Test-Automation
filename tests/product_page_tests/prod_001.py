import allure
import pytest

from tests.base_test import BaseTest


@allure.epic("Madison Island E-Commerce")
@allure.feature("Product Page")
@pytest.mark.usefixtures("function_setup")
class TestProduct(BaseTest):

    @allure.title("Validate product title and price are displayed correctly")
    @allure.description("Verify that the product title and price displayed on the catalog page "
        "match the title and price displayed on the selected product page.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_details_displayed(self):

        with allure.step("Open catalog, select a product, and save its title and price"):
            self.header_area_obj.press_catalog_button()

            catalog_page_product_title = self.catalog_page_obj.get_product_title(3)
            catalog_page_product_price = self.catalog_page_obj.get_product_price(3)

            self.catalog_page_obj.choose_product(3)

        with allure.step("Validate product title and price match the catalog values"):
            assert catalog_page_product_title == self.product_page_obj.get_product_title()
            assert catalog_page_product_price == self.product_page_obj.get_product_price()


    @allure.title("Validate product size selector")
    @allure.description("Verify that the user can select a different product size "
        "and that the selected size remains correctly displayed after reload.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_size_selector_available(self):

        with allure.step("Open catalog, select a product, and choose a different size"):
            self.header_area_obj.press_catalog_button()
            self.catalog_page_obj.choose_product(2)

            expected_size = self.product_page_obj.get_option_size(3)
            self.product_page_obj.choose_size(3)

        with allure.step("Reload the page and validate the selected size"):
            self.product_page_obj.reload_page()

            assert self.product_page_obj.get_selected_size() == expected_size


    @allure.title("Validate product color selector")
    @allure.description("Verify that the user can select a different product color "
        "and that the selected color remains correctly displayed after reload.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_color_selector_available(self):

        with allure.step("Open catalog, select a product, and choose a different color"):
            self.header_area_obj.press_catalog_button()
            self.catalog_page_obj.choose_product(2)

            expected_color = self.product_page_obj.get_option_color(1)
            self.product_page_obj.choose_color(1)

        with allure.step("Reload the page and validate the selected color"):
            self.product_page_obj.reload_page()

            assert self.product_page_obj.get_selected_color() == expected_color


    @allure.title("Validate selected product configuration in cart")
    @allure.description("Verify that the selected product color and size are preserved "
        "after the product is added to the shopping cart.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_validate_cart_product_details(self):

        with allure.step("Open catalog, select a product, choose color and size, and add it to cart"):
            self.header_area_obj.press_catalog_button()
            self.catalog_page_obj.choose_product(2)

            self.product_page_obj.choose_color(1)
            product_color = self.product_page_obj.get_option_color(1)

            self.product_page_obj.choose_size(2)
            product_size = self.product_page_obj.get_option_size(2)

            self.product_page_obj.press_add_cart()

        with allure.step("Validate that the cart contains the selected color and size"):
            product_details = self.cart_page_obj.get_product_details()

            assert product_color in product_details
            assert product_size in product_details
