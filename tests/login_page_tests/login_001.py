import allure
import pytest
from allure_commons.types import Severity
from allure_pytest.utils import allure_description
from tests.base_test import BaseTest
from util.config import ConfigReader

valid_user = ConfigReader.read_list("users", "valid_user")
invalid_users = ConfigReader.read_list("users", "invalid_users")

@pytest.mark.usefixtures("function_setup")
@allure.severity(Severity.NORMAL)
@allure.epic("Login")
class TestLogin(BaseTest):

    @pytest.mark.parametrize("user, password, message", invalid_users)
    @allure.description("Entering the data from config and get valid errors")
    @allure.title("Invalid login check")
    @allure.story("Login is rejected and an error message is displayed")
    def test_invalid_login(self,user, password,message):
        with allure.step("get data from config and then run those 5 tests:"
                         "1. invalid email and check valid error"
                         "2. invalid password and check valid error"
                         "3. empty email and check valid error"
                         "4. empty password and check valid error"
                         "5. invalid email and check valid error"):
            self.header_area_obj.press_login_button()
            self.login_page_obj.login(user,password)
            assert self.login_page_obj.get_error_msg() == message

    @allure.description("Entering the data from config login")
    @allure.title("valid login check")
    @allure.story("Login is rejected and an error message is displayed")
    def test_valid_login(self):
        with allure.step("get data from config and and login"):
            user = valid_user[0]
            password = valid_user[1]
            self.header_area_obj.press_login_button()
            self.login_page_obj.login(user,password)


            assert self.login_page_obj.get_my_account_title() == "My Account"


