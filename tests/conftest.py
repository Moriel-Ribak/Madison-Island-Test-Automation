import allure
import driver
import pytest
from playwright.sync_api import sync_playwright, Page
from components.header_area import HeaderArea
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.forget_pass_page import ForgetPass
from pages.get_5_page import Get5Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage



@pytest.fixture(scope="function")
def function_setup(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://madison-island.com/")

        request.cls.page = page
        request.cls.home_page_obj = HomePage(page)
        request.cls.catalog_page_obj = CatalogPage(page)
        request.cls.get_5_page_obj = Get5Page(page)
        request.cls.header_area_obj = HeaderArea(page)
        request.cls.product_page_obj = ProductPage(page)
        request.cls.cart_page_obj = CartPage(page)
        request.cls.login_page_obj = LoginPage(page)
        request.cls.forget_pass_page_obj = ForgetPass(page)
        request.cls.register_page_obj = RegisterPage(page)

        yield

        page.close()
        browser.close()

@pytest.fixture(scope="class")
def class_setup(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://madison-island.com/")

        request.cls.page = page
        request.cls.home_page_obj = HomePage(page)
        request.cls.catalog_page_obj = CatalogPage(page)
        request.cls.get_5_page_obj = Get5Page(page)
        request.cls.header_area_obj = HeaderArea(page)
        request.cls.product_page_obj = ProductPage(page)
        request.cls.cart_page_obj = CartPage(page)
        request.cls.login_page_obj = LoginPage(page)
        request.cls.forget_pass_page_obj = ForgetPass(page)
        request.cls.register_page_obj = RegisterPage(page)

        yield

        page.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        test_instance = item.instance

        if test_instance is not None:
            page = getattr(test_instance, "page", None)

            if isinstance(page, Page) and not page.is_closed():
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Failed Test Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )