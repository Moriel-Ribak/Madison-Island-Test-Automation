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




