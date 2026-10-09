from components.header_area import HeaderArea
from pages.base_page import BasePage


class HomePage(BasePage):


    def __init__(self, page):
        super().__init__(page)
        self.header_area = HeaderArea(page)

    __SLIDESHOW_CONTROLS = ".slideshow__controls>div>ul>li"
    __SHOP_WOMAN_BUTTON = ".slideshow__btn-wrapper>[href='/collections/women']"
    __SHOP_MAN_BUTTON = ".slideshow__btn-wrapper>[href='/collections/men']"
    __COLLECTION_LIST_TITLE= ".section-header>h2"
    __COLLECTION_LIST_ITEM= ".grid--uniform>li"
    __SLIDESHOW_AREA = ".slick-list"
    __SLIDESHOW_TITLE = ".slideshow__text-content-list>li>h2"




    def press_dots(self,dot_number):
        self.list_click(self.__SLIDESHOW_CONTROLS,dot_number)

    def press_shop_woman_button(self):
        self.press_dots(1)
        self.click(self.__SHOP_WOMAN_BUTTON)

    def press_shop_man_button(self):
        self.press_dots(0)
        self.click(self.__SHOP_MAN_BUTTON)

    def collection_list_title(self):
        return self.get_text(self.__COLLECTION_LIST_TITLE)

    def collection_visible(self):
        collection_list_count = self.count(self.__COLLECTION_LIST_ITEM)
        for section in range(collection_list_count):
            if not self.is_list_item_visible(self.__COLLECTION_LIST_ITEM, section):
                return False

        return True

    def slideshow_visible(self):
       return self.is_visible(self.__SLIDESHOW_AREA)


    def collection_click(self,index):
        self.list_click(self.__COLLECTION_LIST_ITEM,index)

    def get_slideshow_title(self,index):
        return self.list_get_text(self.__SLIDESHOW_TITLE,index)

    def get_slideshow_area(self):
        return self.count(self.__SLIDESHOW_TITLE)



