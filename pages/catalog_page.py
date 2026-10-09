from playwright.sync_api import Page
from components.header_area import HeaderArea
from pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.__header_area = HeaderArea(page)

    __PRODUCT = ".grid.grid--uniform>li"
    __PRODUCT_CARD = ".grid-view-item>dl"
    __PRODUCT_TITLE = ".grid.grid--uniform>li>div>a>span"
    __PRODUCT_PRICE = ".price-item.price-item--regular"
    __SALE_PRODUCT_PRICE = ".price-item--sale"
    __CATALOG_TITLE = "h1>span[role='text']"
    __SEARCH_RESULTS_AREA = ".page-width.list-view-items"
    __SEARCH_PRODUCT_LIST = ".page-width>li"
    __SEARCH_PRODUCT_TITLE = f"{__SEARCH_PRODUCT_LIST}>div>a>span"
    __START_END_PAGE = "li>button"
    __NEXT_PAGE = "li>a>.icon-arrow-right"
    __PRODUCT_COUNT_TEXT = ".filters-toolbar__product-count"
    __SORT_BY = "#SortBy"
    __PAGE_NUMBERS=".pagination__text"

    def choose_product(self, index):
        self.list_click(self.__PRODUCT, index)

    def get_product_title(self, index):
        return self.list_get_text(self.__PRODUCT_TITLE, index)

    def get_product_price(self, index):
        product_card = self.page.locator(self.__PRODUCT_CARD).nth(index)

        if "price--on-sale" in product_card.get_attribute("class"):
            return product_card.locator(self.__SALE_PRODUCT_PRICE).inner_text()
        else:
            return product_card.locator(self.__PRODUCT_PRICE).inner_text()

    def get_title(self):
        text = self.get_text(self.__CATALOG_TITLE)
        return text.replace("Collection:", "").strip()

    def search_results_visible(self):
        return self.is_visible(self.__SEARCH_RESULTS_AREA)

    def get_search_list_item_title(self):
        return self.list_get_text(self.__SEARCH_PRODUCT_TITLE, 0)

    def get_search_list_count(self):
        return self.count(self.__SEARCH_PRODUCT_LIST)

    def check_if_last_page(self):
        return self.is_visible(self.__START_END_PAGE)

    def press_next_page(self):
        self.click(self.__NEXT_PAGE)

    def count_page_products(self):
        return self.count(self.__PRODUCT_TITLE)

    def get_product_count_text(self):
        return self.get_text(self.__PRODUCT_COUNT_TEXT)

    def is_details_visible(self, index):
        return self.list_is_visible(self.__PRODUCT_TITLE, index) and self.list_is_visible(self.__PRODUCT_PRICE, index)

    def select_sort(self, index):
        self.select_option(self.__SORT_BY, index)

    def get_page_numbers_text(self):
        return self.get_text(self.__PAGE_NUMBERS)
