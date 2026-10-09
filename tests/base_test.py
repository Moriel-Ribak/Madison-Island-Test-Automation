from components.header_area import HeaderArea
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.forget_pass_page import ForgetPass
from pages.get_5_page import Get5Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage


class BaseTest:
    home_page_obj : HomePage
    catalog_page_obj : CatalogPage
    get_5_page_obj : Get5Page
    header_area_obj : HeaderArea
    product_page_obj : ProductPage
    cart_page_obj : CartPage
    login_page_obj : LoginPage
    forget_pass_page_obj : ForgetPass
    register_page_obj : RegisterPage