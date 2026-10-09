import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.epic("Navigation")
@allure.severity(Severity.CRITICAL)
class TestHomePageNavigations(BaseTest):
        @allure.description("Press any section and validate title")
        @allure.title("Collection navigations checks")
        @allure.story("Collections pages open")
        def test_navigate_woman(self):
            with allure.step("press the Woman section and checks title"):
                self.home_page_obj.collection_click(0)
                assert self.catalog_page_obj.get_title() == "Women"

        def test_navigate_man(self):
            with allure.step("press the Man section and checks title"):
                self.home_page_obj.collection_click(1)

                with allure.step("Take screenshot"):
                    allure.attach(
                        self.page.screenshot(full_page=True),
                        name="Empty Cart",
                        attachment_type=allure.attachment_type.PNG
                    )

                assert self.catalog_page_obj.get_title() == "Men"

        def test_navigate_accessories(self):
            with allure.step("press the Accessories section and checks title"):
                self.home_page_obj.collection_click(2)
                assert self.catalog_page_obj.get_title() == "Accessories"

        def test_navigate_homeDecor(self):
            with allure.step("press the Home & Decor section and checks title"):
                self.home_page_obj.collection_click(3)
                assert self.catalog_page_obj.get_title() == "Home & Decor"
