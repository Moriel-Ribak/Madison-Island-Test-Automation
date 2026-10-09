import time

import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest

@pytest.mark.usefixtures("function_setup")
@allure.epic("UI")
@allure.severity(Severity.NORMAL)
class TestHomePageCollection(BaseTest):

    @allure.title("Main collection sections are displayed")
    @allure.description(
        "Verify that all main collection sections are visible on the home page."
    )
    @allure.story("Home page collections")
    def test_collections_visible(self):
        with allure.step("Verify all collection sections are visible"):
            assert self.home_page_obj.collection_visible()


    @allure.title("Home pagef functional")
    @allure.description("Homepage loads successfully and the main home content is displayed")
    @allure.story("Homepage loads successfully and the main home content is displayed")
    def test_functional_homepage(self):
        with allure.step("checks if the url is currect and if the slide show and collections are visible"):
            assert self.home_page_obj.get_url() == "https://madison-island.com/"
            assert self.home_page_obj.collection_list_title() == "COLLECTION LIST"
            assert  self.home_page_obj.collection_visible() == True
            assert  self.home_page_obj.slideshow_visible() == True



    @allure.title("Dot navigations checks")
    @allure.description("Press every dot and check that the active slide changed")
    @allure.story("The selected hero slide becomes active and its content is displayed")
    def test_slideshow_check(self):
        with allure.step("get slideshow area and get the first title"):
            slideshow_area = self.home_page_obj.get_slideshow_area()
            last_slide_title = self.home_page_obj.get_slideshow_title(0)
        with allure.step("loop on all the dots and compare the active slide title to the last"):
            for i in range(1, slideshow_area):
                self.home_page_obj.press_dots(i)
                time.sleep(2)
                active_slide_title = self.home_page_obj.get_slideshow_title(i)
                assert active_slide_title != last_slide_title
                last_slide_title = active_slide_title
