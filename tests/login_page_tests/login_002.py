import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest


@pytest.mark.usefixtures("function_setup")
@allure.severity(Severity.MINOR)
@allure.epic("Login")
class TestLogin(BaseTest):

    @allure.description("entering the website and validate by title")
    @allure.title("Forget password page validation")
    @allure.story("Password reset section/form is displayed")
    def test_forget_password(self):
        with allure.step("verify Reset password page by checking the title"):
            self.header_area_obj.press_login_button()
            self.login_page_obj.click_forget_password()
            assert self.forget_pass_page_obj.get_forget_pass_title() == "RESET YOUR PASSWORD"


    @allure.description("entering the website pressing cancel and validate by title")
    @allure.title("Forget password cancel button validation")
    @allure.story("Reset form closes or returns user to login state")
    def test_cancel_forget_pass(self):
        with allure.step("cancel button going back to log in page"):
            self.header_area_obj.press_login_button()
            self.login_page_obj.click_forget_password()
            self.forget_pass_page_obj.press_cancel()
            assert self.login_page_obj.get_login_title() == "Login"

