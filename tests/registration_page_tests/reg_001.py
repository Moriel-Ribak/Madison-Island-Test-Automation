import allure
import pytest
from tests.base_test import BaseTest
from util.config import ConfigReader

invalid_register = ConfigReader.read_list("register_user", "invalid_register")
valid_register = ConfigReader.read_list("register_user", "valid_register")
no_data_register = ConfigReader.read_list("register_user","no_data_register")

@allure.epic("Register page")
@pytest.mark.usefixtures("function_setup")
@allure.severity(allure.severity_level.BLOCKER)
class TestRegisterPage(BaseTest):

    def navigate_to_register(self):
        with allure.step("Navigate to the registration page"):
            self.header_area_obj.press_login_button()
            self.login_page_obj.click_register()

    @allure.title("Validate registration page is displayed")
    def test_verify_register_page(self):
        self.navigate_to_register()

        with allure.step("Validate page title"):
            assert self.register_page_obj.get_page_title() == "Create Account"

    @allure.title("Validate registration with missing required fields")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name,last_name,email,password,error_msg", invalid_register)
    def test_invalid_register(self, first_name, last_name, email, password, error_msg):
        self.navigate_to_register()

        with allure.step("Fill registration form with invalid data and create account"):
            self.register_page_obj.fill_first_name(first_name)
            self.register_page_obj.fill_last_name(last_name)
            self.register_page_obj.fill_email(email)
            self.register_page_obj.fill_password(password)
            self.register_page_obj.press_create()

        with allure.step("Validate error message"):
            assert self.register_page_obj.get_error_msg(0) == error_msg

    @allure.title("Validate successful user registration")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name,last_name,email,password", valid_register)
    def test_valid_register(self, first_name, last_name, email, password):
        self.navigate_to_register()

        with allure.step("Fill registration form with valid data and create account"):
            self.register_page_obj.fill_first_name(first_name)
            self.register_page_obj.fill_last_name(last_name)
            self.register_page_obj.fill_email(email)
            self.register_page_obj.fill_password(password)
            self.register_page_obj.press_create()

        with allure.step("Validate successful registration redirect"):
            self.register_page_obj.wait_for_url("https://madison-island.com/")

        with allure.step("Open account page"):
            self.header_area_obj.press_login_button()

        with allure.step("Validate account page"):
            assert self.register_page_obj.wait_for_url("https://madison-island.com/account")

    @allure.title("Validate registration with multiple empty required fields")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name,last_name,email,password,error1,error2", no_data_register)
    def test_no_data_register(self, first_name, last_name, email, password, error1, error2):
        self.navigate_to_register()

        with allure.step("Submit registration form with multiple required fields left empty"):
            self.register_page_obj.fill_first_name(first_name)
            self.register_page_obj.fill_last_name(last_name)
            self.register_page_obj.fill_email(email)
            self.register_page_obj.fill_password(password)
            self.register_page_obj.press_create()

        with allure.step("Validate error messages"):
            assert self.register_page_obj.get_error_msg(0) == error1
            assert self.register_page_obj.get_error_msg(1) == error2